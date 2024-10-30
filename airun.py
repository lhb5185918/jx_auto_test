from flask import Flask, render_template, request, jsonify
# from openai import OpenAI  # 注释掉 OpenAI 的导入
import qianfan  # 导入 Qianfan 库
import markdown
from utils.get_yaml_data import *

app = Flask(__name__)

# 使用 Qianfan 的 AccessKey 和 SecretKey
chat_completion = qianfan.ChatCompletion(
)
# 用于存储对话历史
conversation_history = []


# 用于计数对话次数


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message')
    # 将用户输入转换为 Markdown 格式
    markdown_input = markdown.markdown(user_input)
    test_results = read_yaml(Path.test_result_data, 'result_data', 'data')

    # 检查 total 是否为零，避免除零错误
    if test_results['total'] == 0:
        return jsonify({'error': '没有执行任何测试用例，无法计算通过率和失败率。'}), 400

    fail_rate = (test_results['failed'] / test_results['total']) * 100
    pass_rate = (test_results['passed'] / test_results['total']) * 100

    prompt = f"""
           你是一名软件测试工程师，负责根据自动化测试用例的执行结果进行深入分析，并撰写一份专业的测试报告。

           ### 执行结果概述：
           1. **接口自动化测试结果**:
              - **执行用例总数**: {test_results['total']}
              - **成功用例数**: {test_results['passed']}
              - **失败用例数**: {test_results['failed']}
              - **失败的用例**: {test_results['failed_tests'][0] if test_results['failed_tests'] else '无'}
                - **失败的日志**: {test_results['failed_logs'][0]['test_name'] + ": " + test_results['failed_logs'][0]['error'] if test_results['failed_logs'] else '无'}
              - **响应时间超过2秒的用例**: 
                - {', '.join([f"{test[0]} (耗时: {test[1]:.2f}s)" for test in test_results['slow_tests']])}

           ### 分析报告内容：
           1. **通过率和失败率分析**:
              - 本次自动化测试的通过率为 {pass_rate:.2f}%，失败率为 {fail_rate:.2f}%。通过率和失败率的计算公式为：
                - 通过率 = (成功用例数 / 执行用例总数) * 100
                - 失败率 = (失败用例数 / 执行用例总数) * 100

           2. **失败用例分析**:
              - 失败的用例为 `{test_results['failed_tests'] if test_results['failed_tests'] else '无'}`，失败原因是 `{test_results['failed_logs'] if test_results['failed_logs'] else '无'}`。

           3. **性能分析**:
              - 响应时间超过2秒的用例表明系统在处理某些请求时存在性能瓶颈。建议对这些用例进行深入分析，找出性能问题的根源并进行优化。

           请根据以上分析，生成针对于本次自动化测试情况生成总结。
       """

    # 增加用户输入到对话历史
    conversation_history.append({'role': 'user', 'content': user_input})

    # 增加提示词到对话历史
    conversation_history.append({'role': 'user', 'content': prompt + markdown_input})

    # 确保在调用 API 之前，conversation_history 不为空
    if not conversation_history:
        return jsonify({'error': '对话历史为空，无法调用 Qianfan API。'}), 400

    try:
        # 调用 Qianfan API
        resp = chat_completion.do(model="ERNIE-Speed-128K", messages=conversation_history)
        print("API response:", resp)  # 打印 API 响应以检查其结构

        # 从 body 中提取 result 字段
        response_content = resp.body.get('result', '')

        # 将模型的响应添加到对话历史
        conversation_history.append({'role': 'assistant', 'content': response_content})

        return jsonify({'response': response_content})
    except Exception as e:
        print(f"Error calling Qianfan API: {e}")
        return jsonify({'error': '调用 Qianfan API 时出错。'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
