import pytest
import requests
from utils.get_yaml_data import *
from config.path import Path
import json
import time
from utils.time_decorator import ResponseTimeRecorder


def get_case_chinese_name(item):
    """获取测试用例的中文名称"""
    # 首先尝试从测试用例的参数中获取title
    try:
        if hasattr(item, 'callspec') and hasattr(item.callspec, 'params'):
            for param_name, param_value in item.callspec.params.items():
                if isinstance(param_value, dict) and 'title' in param_value:
                    return param_value['title']
    except Exception as e:
        print(f"从测试用例参数获取title失败: {str(e)}")

    # 尝试从yaml文件中获取title
    try:
        # 获取测试函数名
        test_name = item.name
        # 从测试函数名中提取yaml中的key
        yaml_key = '_'.join(test_name.split('_')[1:])
        if '[' in yaml_key:  # 处理参数化测试用例名称
            yaml_key = yaml_key.split('[')[0]
        
        # 获取测试文件路径
        test_file = item.fspath.strpath
        # 获取测试文件名（不含路径和扩展名）
        test_file_name = test_file.split('\\')[-1].replace('test_', '').replace('.py', '')
        # 构建yaml文件路径
        yaml_file = f"{Path.testdata_path}/{test_file_name}_data.yaml"
        
        # 读取yaml文件
        yaml_data = read_yaml(yaml_file)
        if yaml_data and yaml_key in yaml_data:
            # 获取对应接口的title
            api_data = yaml_data[yaml_key]
            if isinstance(api_data, list) and api_data and 'title' in api_data[0]:
                return api_data[0]['title']
    except Exception as e:
        print(f"从yaml获取title失败: {str(e)}")
    
    # 如果从yaml获取失败，尝试从allure标记获取
    epic = ""
    feature = ""
    story = ""
    for marker in item.iter_markers():
        if marker.name == "allure_label":
            if marker.kwargs.get("label_type") == "epic":
                epic = marker.kwargs.get("value")
            elif marker.kwargs.get("label_type") == "feature":
                feature = marker.kwargs.get("value")
            elif marker.kwargs.get("label_type") == "story":
                story = marker.kwargs.get("value")

    # 如果没有通过 marker 获取到，尝试从 item._obj 获取
    if hasattr(item, "_obj"):
        test_func = item._obj
        if hasattr(test_func, "__dict__"):
            for key, value in test_func.__dict__.items():
                if key.startswith("_allure"):
                    if "epic" in str(value):
                        epic = str(value).split('"')[1]
                    elif "feature" in str(value):
                        feature = str(value).split('"')[1]
                    elif "story" in str(value):
                        story = str(value).split('"')[1]

    # 组合中文名称
    chinese_name = f"{story}"
    return chinese_name if chinese_name else item.name


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
    try:
        headers = {"Content-Type": "application/json"}
        data = {
            "msgtype": "text",
            "text": {
                "content": message
            }
        }
        print(f"正在发送钉钉消息，webhook_url: {webhook_url}")
        print(f"发送的消息内容: {message}")
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        response_json = response.json()
        print(f"钉钉返回结果: {response_json}")
        return response_json
    except Exception as e:
        print(f"发送钉钉消息失败: {str(e)}")
        return {"errcode": -1, "errmsg": str(e)}


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
    if call.when == "call":
        test_results["total"] += 1
        
        test_name = get_case_chinese_name(item)
        if not test_name:
            test_name = item.name

        if call.excinfo is None:
            test_results["passed"] += 1
        else:
            test_results["failed"] += 1
            test_results["failed_tests"].append(test_name)
            error_message = str(call.excinfo.value)
            test_results["failed_logs"].append({
                "test_name": test_name,
                "error": error_message
            })

        # 获取实际接口响应时间（毫秒）
        actual_response_time = ResponseTimeRecorder.get_time(item.name)
        
        # 记录所有接口的响应时间
        if actual_response_time > 0:  # 如果有记录实际响应时间
            test_results.setdefault("response_times", []).append({
                "name": test_name,
                "time": actual_response_time,
                "type": "接口响应",
                "is_slow": actual_response_time > 3000
            })
        else:  # 如果没有记录实际响应时间，使用原有的方式（转换为毫秒）
            case_time = call.duration * 1000  # 转换为毫秒
            test_results.setdefault("response_times", []).append({
                "name": test_name,
                "time": case_time,
                "type": "用例执行",
                "is_slow": case_time > 3000
            })


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_sessionfinish(session, exitstatus):
    yield
    # 从配置文件中读取webhook URL
    try:
        webhook_url = read_yaml(Path.config_file_path, 'dingtalk', 'webhook_url')
    except:
        webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=65d54ed9f20a4ea01c7fc02bda39a21a49bccbe746b20be9a074d281b0828167"
        print("未能从配置文件读取钉钉webhook URL，使用默认URL")

    # 计算通过率
    pass_rate = (test_results['passed'] / test_results['total'] * 100) if test_results['total'] > 0 else 0

    message = (
        f"【test】接口自动化测试报告\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 测试结果统计\n"
        f"• 总用例数: {test_results['total']}\n"
        f"• 通过用例: {test_results['passed']}\n"
        f"• 失败用例: {test_results['failed']}\n"
        f"• 通过率: {pass_rate:.1f}%\n"
    )
    
    # 如果有失败的用例，添加详细信息
    if test_results['failed_tests']:
        message += f"\n❌ 失败用例详情\n"
        for log in test_results['failed_logs']:
            error_msg = log['error']
            # 处理AssertionError类型的错误
            if 'AssertionError' in error_msg:
                if "==" in error_msg:
                    actual_result = error_msg.split("assert")[1].split("==")[0].strip().strip("('").strip("'")
                    error_msg = actual_result
                else:
                    error_msg = error_msg.replace("AssertionError: ", "").split("\n")[0]
            elif 'TypeError' in error_msg:
                error_msg = error_msg.split(": ")[1] if ": " in error_msg else error_msg
            
            message += (
                f"• {log['test_name']}\n"
                f"  错误原因: {error_msg}\n"
            )
    
    # 添加所有接口的响应时间信息
    if test_results.get('response_times'):
        message += f"\n⏱️ 接口响应时间统计\n"
        
        # 按响应时间排序（从高到低）
        sorted_times = sorted(test_results['response_times'], key=lambda x: x['time'], reverse=True)
        
        # 分类显示
        slow_apis = [t for t in sorted_times if t['is_slow']]
        normal_apis = [t for t in sorted_times if not t['is_slow']]
        
        # 显示超时的接口
        if slow_apis:
            message += "❗响应超时(>3000ms)的接口:\n"
            for test in slow_apis:
                message += f"• {test['name']} ({test['type']}耗时: {test['time']:.0f}ms)\n"
            message += "\n"
            
        # 显示正常的接口
        if normal_apis:
            message += "✅ 响应正常的接口:\n"
            for test in normal_apis:
                message += f"• {test['name']} ({test['type']}耗时: {test['time']:.0f}ms)\n"

    # 添加报告链接
    message += (
        f"\n📋 详细报告\n"
        f"• 测试报告: http://192.168.111.45:8080\n"
        f"• AI分析: http://192.168.111.45:5000\n"
        f"━━━━━━━━━━━━━━━━━━━━━━"
    )

    print("准备发送测试结果到钉钉...")
    write_yaml(Path.test_result_data, "result_data", "data", test_results, None)
    send_result = send_to_dingtalk(webhook_url, message)
    print(f"钉钉消息发送完成，结果: {send_result}")


@pytest.fixture(autouse=True)
def clear_response_times():
    """每次测试会话开始时清除响应时间记录"""
    ResponseTimeRecorder.clear()
    yield
