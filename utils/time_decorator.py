import time
import functools
from typing import Dict, Any
import inspect

class ResponseTimeRecorder:
    """响应时间记录器"""
    _instance = None
    _response_times: Dict[str, float] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ResponseTimeRecorder, cls).__new__(cls)
        return cls._instance

    @classmethod
    def record_time(cls, test_name: str, response_time: float):
        """记录响应时间"""
        cls._response_times[test_name] = response_time

    @classmethod
    def get_time(cls, test_name: str) -> float:
        """获取响应时间"""
        return cls._response_times.get(test_name, 0.0)

    @classmethod
    def clear(cls):
        """清除所有记录"""
        cls._response_times.clear()

def record_response_time(func):
    """
    装饰器：记录接口响应时间
    使用方法：在需要记录响应时间的接口请求方法上添加此装饰器
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 记录开始时间
        start_time = time.time()
        
        # 执行请求
        result = func(*args, **kwargs)
        
        # 计算响应时间
        response_time = time.time() - start_time
        
        # 获取当前调用栈
        current_frame = inspect.currentframe()
        try:
            # 向上遍历调用栈
            while current_frame:
                # 获取调用方的代码对象
                code_obj = current_frame.f_code
                # 如果是测试方法（以test_开头）
                if code_obj.co_name.startswith('test_'):
                    # 获取完整的测试名称（包括参数化的情况）
                    f_locals = current_frame.f_locals
                    if 'self' in f_locals:
                        test_instance = f_locals['self']
                        if hasattr(test_instance, '_testMethodName'):
                            test_name = test_instance._testMethodName
                        else:
                            test_name = code_obj.co_name
                    else:
                        test_name = code_obj.co_name
                    break
                current_frame = current_frame.f_back
            else:
                # 如果没找到测试方法，使用被装饰函数的名称
                test_name = func.__name__
        finally:
            # 清理引用，避免内存泄漏
            del current_frame
        
        # 记录响应时间
        ResponseTimeRecorder.record_time(test_name, response_time)
        return result
    return wrapper 