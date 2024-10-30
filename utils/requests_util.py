import requests
import logging
import time
import inspect
from utils.time_decorator import ResponseTimeRecorder


class Request:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # 创建一个handler，用于写入日志文件
        fh = logging.StreamHandler()
        fh.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)

    def _get_test_name(self):
        """获取当前测试用例名称"""
        current_frame = inspect.currentframe()
        try:
            while current_frame:
                code_obj = current_frame.f_code
                if code_obj.co_name.startswith('test_'):
                    f_locals = current_frame.f_locals
                    if 'self' in f_locals:
                        test_instance = f_locals['self']
                        if hasattr(test_instance, '_testMethodName'):
                            return test_instance._testMethodName
                    return code_obj.co_name
                current_frame = current_frame.f_back
        finally:
            del current_frame
        return None

    def api_run(self, url, method, data=None, headers=None, cookie=None, file=None, filename=None,
                file_path=None):
        # 记录开始时间
        start_time = time.time()
        
        if method == 'post':
            if file is not None:
                files = {str(file): (str(filename), open(str(file_path), 'rb'),
                                     'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
                res = requests.post(url=url, headers=headers, json=data, files=files)
            else:
                res = requests.post(url=url, headers=headers, json=data)
        else:
            res = requests.get(url=url, headers=headers)

        # 计算响应时间（转换为毫秒）
        response_time = (time.time() - start_time) * 1000
        
        # 获取并记录测试用例名称和响应时间
        test_name = self._get_test_name()
        if test_name:
            ResponseTimeRecorder.record_time(test_name, response_time)

        code = res.status_code
        cookies = res.cookies.get_dict()
        dict1 = dict()  # 创建空列表
        try:
            body = res.json()  # 接收返回json格式的响应
        except ValueError:
            body = res.text  # 接收返回text格式的响应报文
        dict1['code'] = code
        dict1['body'] = body
        dict1['cookies'] = cookies
        dict1['response_time'] = response_time  # 添加响应时间（毫秒）到返回结果中
        
        self.logger.info(
            f"URL: {url}, Method: {method}, Response Time: {response_time:.2f}ms, Response Code: {code}, Response Body: {body}, Request Data: {data}")
        return dict1

    def send(self, url, method, **kwargs):
        return self.api_run(url=url, method=method, **kwargs)
