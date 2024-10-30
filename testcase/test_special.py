import pytest
from config.path import *
from utils.get_yaml_data import *
from utils.requests_util import Request
from utils.log import logger
from utils.other_utils import *
from utils.mysql_util import CommonDatabase
import requests
import allure


class TestSpecialData:
    create_special_order = read_yaml(Path.special_data_path, 'create_special_order')
    select_special_order_detail_info = read_yaml(Path.special_data_path, 'select_special_order_detail_info')

    @allure.title("特殊订单新增")
    @pytest.mark.parametrize("create_special_order", create_special_order)  # 特殊订单新增
    def test_create_special_order(self, create_special_order, get_token):
        create_special_order['data']['origNo'] = f"test-special-{random.randint(100000, 999999)}"
        result = Request().send(url=create_special_order["url"],
                                method=create_special_order["method"],
                                data=create_special_order["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == "成功"
        write_yaml(Path.special_middle_path, "special_order_data", "data", create_special_order['data']['origNo'],
                   dict_key=None)

    @allure.title("特殊订单列表查询接口")
    @pytest.mark.parametrize("select_special_order_detail_info", select_special_order_detail_info)  # 特殊订单列表查询接口
    def test_select_special_order_detail_info(self, select_special_order_detail_info, get_token):
        select_special_order_detail_info['data']['orderNo'] = read_yaml(Path.special_middle_path, "special_order_data",
                                                                        "data")
        result = Request().send(url=select_special_order_detail_info["url"],
                                method=select_special_order_detail_info["method"],
                                data=select_special_order_detail_info["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == "成功"
