import pytest
import requests
from utils.get_yaml_data import *
from config.path import Path
import random
import json


@pytest.fixture(scope='session')
def get_token():
    url = read_yaml(Path.config_file_path, 'login_data', 'url')
    data = {"userNo": "lhb001",
            "pwd": "lhx7758521",
            "platForm": "app",
            "companyCode": "ZHQC",
            "whId": 1,
            "warehouseId": "",
            "haveWarehouse": 1,
            "clientId": "iowtb-new",
            "userLanguage": "zh-CN"}
    res = requests.post(url=url, json=data, headers={'Content-Type': 'application/json'})
    token = res.json()['obj']['token']
    headers = {'Content-Type': 'application/json', 'Authorization': token}
    return headers


def send_to_dingtalk(webhook_url, message):
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    return response.json()


# 用于存储测试结果
test_results = {
    "total": 0,
    "passed": 0,
    "failed": 0,
    "failed_tests": []
}


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    yield
    if call.when == "call":  # 只在测试执行阶段处理结果
        test_results["total"] += 1
        if call.excinfo is None:  # 测试通过
            test_results["passed"] += 1
        else:  # 测试失败
            test_results["failed"] += 1
            test_results["failed_tests"].append(item.name)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_sessionfinish(session, exitstatus):
    yield
    # 测试结束后发送总结信息
    webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=65d54ed9f20a4ea01c7fc02bda39a21a49bccbe746b20be9a074d281b0828167"
    message = (
        f"测试总结:\n"
        f"总共执行用例: {test_results['total']}\n"
        f"成功用例: {test_results['passed']}\n"
        f"失败用例: {test_results['failed']}\n"
        f"失败的用例: {', '.join(test_results['failed_tests']) if test_results['failed_tests'] else '无'}\n"
    )

    send_to_dingtalk(webhook_url, message)
