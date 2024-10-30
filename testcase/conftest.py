import pytest
import requests
from utils.get_yaml_data import *
from config.path import Path
import json
import time


@pytest.fixture(scope='session')
def get_token():
    url = read_yaml(Path.config_file_path, 'login_data', 'url')
    data = {
        "userNo": "lhb001",
        "pwd": "lhx7758521",
        "platForm": "app",
        "companyCode": "ZHQC",
        "whId": 1,
        "warehouseId": "",
        "haveWarehouse": 1,
        "clientId": "iowtb-new",
        "userLanguage": "zh-CN"
    }
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
    "failed_tests": [],
    "slow_tests": [],
    "failed_logs": []  # 新增字段用于存储失败日志
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
            # 记录失败的日志信息
            error_message = str(call.excinfo.value)  # 获取异常信息
            test_results["failed_logs"].append({
                "test_name": item.name,
                "error": error_message
            })

        # 记录响应时间
        response_time = call.duration  # 获取测试用例的执行时间
        if response_time > 3:  # 如果响应时间超过2秒
            test_results["slow_tests"].append((item.name, response_time))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_sessionfinish(session, exitstatus):
    yield
    # 测试结束后发送总结信息
    webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=65d54ed9f20a4ea01c7fc02bda39a21a49bccbe746b20be9a074d281b0828167"

    # 构建错误日志信息
    failed_logs_message = "\n".join([f"{log['test_name']}: {log['error']}" for log in test_results['failed_logs']]) if \
        test_results['failed_logs'] else '无'

    message = (
        f"接口自动化测试结果:\n"
        f"执行用例总数: {test_results['total']}\n"
        f"成功用例数: {test_results['passed']}\n"
        f"失败用例数: {test_results['failed']}\n"
        f"失败的用例: {', '.join(test_results['failed_tests']) if test_results['failed_tests'] else '无'}\n"
        f"失败的日志: {failed_logs_message}\n"  # 添加失败日志信息
        f"响应时间超过2秒的用例: {', '.join([f'{name} (耗时: {time:.2f}s)' for name, time in test_results['slow_tests']]) if test_results['slow_tests'] else '无'}\n"
        f"测试报告地址:http://192.168.111.45:8080\n"
        f"基线自动化AI地址:http://192.168.111.45:5000\n"
    )
    write_yaml(Path.test_result_data, "result_data", "data", test_results, None)
    send_to_dingtalk(webhook_url, message)
