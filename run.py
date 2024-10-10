import pytest
import os
from flask import Flask, send_from_directory
import subprocess
import os
from flask import Flask, send_from_directory

import pytest
import os
from flask import Flask, send_from_directory


def run_tests_and_generate_report():
    # 设置工作目录为脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(f"当前工作目录: {os.getcwd()}")

    # 运行 pytest 并生成 allure 结果
    pytest.main(['-s', '-v', '--alluredir', './target/allure-results', '--clean-alluredir'])

    # 确保 allure-results 目录存在
    if not os.path.exists('./target/allure-results'):
        print("allure-results 目录不存在，创建目录")
        os.makedirs('./target/allure-results')

    # 生成 Allure 报告
    os.system('allure generate ./target/allure-results -o ./target/allure-report --clean')


# 运行命令生成 Allure 报告
run_tests_and_generate_report()

# 创建 Flask 应用
app = Flask(__name__, static_folder='./target/allure-report')


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
