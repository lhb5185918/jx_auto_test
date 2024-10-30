class AssertionUtil:

    @staticmethod
    def assert_operate(result):  # 操作类接口断言
        if result['body']['code'] != 200:
            raise AssertionError('接口返回状态码错误,接口执行失败')
        else:
            if result['body']['msg'] == "成功":
                return True
            else:
                raise AssertionError('接口返回信息错误,接口执行失败')

    @staticmethod
    def assert_select(result):
        if result['body']['code'] != 200:
            raise AssertionError('接口返回状态码错误,接口执行失败')
        else:
            if result['body']['msg'] == "成功":
                if isinstance(result['body']['obj'], dict):
                    if result['body']['obj'] is not None:
                        return True
                    else:
                        return {"success": False, "msg": "查询接口返回数据为空"}
                else:
                    if result['body']['obj'][0] is not None:
                        return True
                    else:
                        return {"success": False, "msg": "查询接口返回数据为空"}
            else:
                raise AssertionError('接口返回信息错误,接口执行失败')
