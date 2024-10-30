import pytest
from config.path import *
from utils.get_yaml_data import *
from utils.requests_util import Request
from utils.log import logger
from utils.other_utils import *
from utils.mysql_util import CommonDatabase
import requests
import allure


class TestOutOrderData:
    out_order_select_data = read_yaml(Path.out_order_data_path, 'out_order_select_data')
    create_out_order = read_yaml(Path.out_order_data_path, 'create_out_order')
    make_out_order_data = read_yaml(Path.out_order_data_path, 'make_out_order_data')
    select_out_order_detail_data = read_yaml(Path.out_order_data_path, 'select_out_order_detail_data')
    so_allocation_page_info = read_yaml(Path.out_order_data_path, 'so_allocation_page_info')
    so_allocation_data = read_yaml(Path.out_order_data_path, 'so_allocation_data')
    so_allocation_detail_page_info = read_yaml(Path.out_order_data_path, 'so_allocation_detail_page_info')
    so_page_info = read_yaml(Path.out_order_data_path, 'so_page_info')
    so_detail_info = read_yaml(Path.out_order_data_path, 'so_detail_info')

    @allure.title("出库订单查询接口")
    @pytest.mark.order(1)
    @pytest.mark.parametrize("out_order_select_data", out_order_select_data)  # 出库订单查询接口
    def test_out_order_select_data(self, out_order_select_data, get_token):
        result = Request().send(url=out_order_select_data["url"], method=out_order_select_data["method"],
                                data=out_order_select_data["data"],
                                headers=get_token)
        logger.info(out_order_select_data['title'], result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("出库订单新增接口")
    @pytest.mark.order(2)
    @pytest.mark.parametrize("create_out_order", create_out_order)  # 出库订单新增接口
    def test_create_out_order(self, create_out_order, get_token):
        create_out_order['data']['origNo'] = f"auto-test{generate_random_number()}"
        result = Request().send(url=create_out_order["url"], method=create_out_order["method"],
                                data=create_out_order["data"],
                                headers=get_token)
        logger.info(create_out_order['title'], result)
        assert result['code'] == 200 and result["body"] is not None
        write_yaml(Path.out_order_middle_path, "order_no", "data",
                   create_out_order['data']['origNo'],
                   None)

    @allure.title("tob出库订单生成接口")
    @pytest.mark.order(3)
    @pytest.mark.parametrize("make_out_order_data", make_out_order_data)  # tob订单生成接口
    def test_make_out_order_data(self, make_out_order_data, get_token):
        detail_id = CommonDatabase().select_data("id", "order_tt_out_order",
                                                 f"orig_no = '{read_yaml(Path.out_order_middle_path, 'order_no', 'data')}'")[
            'id']
        result = Request().send(url=make_out_order_data["url"], method=make_out_order_data["method"],
                                data=[f"{detail_id}"],
                                headers=get_token)
        logger.info(make_out_order_data['title'], result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("tobso查看接口")
    @pytest.mark.order(4)
    @pytest.mark.parametrize("select_out_order_detail_data", select_out_order_detail_data)  # tobso查看接口
    def test_select_out_order_detail_data(self, select_out_order_detail_data, get_token):
        detail_id = CommonDatabase().select_data("id", "order_tt_out_order",
                                                 f"orig_no = '{read_yaml(Path.out_order_middle_path, 'order_no', 'data')}'")[
            'id']
        result = Request().send(url=select_out_order_detail_data["url"] + str(detail_id),
                                method=select_out_order_detail_data["method"],
                                headers=get_token)
        logger.info(select_out_order_detail_data['title'], result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("so分配l列表查询接口")
    @pytest.mark.order(5)
    @pytest.mark.parametrize("so_allocation_page_info", so_allocation_page_info)  # so分配列表查询接口
    def test_so_allocation_page_info(self, so_allocation_page_info, get_token):
        result = Request().send(url=so_allocation_page_info["url"], method=so_allocation_page_info["method"],
                                data=so_allocation_page_info["data"],
                                headers=get_token)
        logger.info(so_allocation_page_info['title'], result)
        assert result['code'] == 200 and result["body"] is not None
        write_yaml(Path.out_order_middle_path, "so_id", "data",
                   result['body']['obj'][0]['id'],
                   None)

    @allure.title("so手动分配接口")
    @pytest.mark.order(6)
    @pytest.mark.parametrize("so_allocation_data", so_allocation_data)  # so手动分配接口
    def test_so_allocation_data(self, so_allocation_data, get_token):
        result = Request().send(url=so_allocation_data["url"], method=so_allocation_data["method"],
                                data=[f'{read_yaml(Path.out_order_middle_path, "so_id", "data")}'],
                                headers=get_token)
        logger.info(so_allocation_data['title'], result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("so查看详情接口")
    @pytest.mark.order(7)
    @pytest.mark.parametrize("so_allocation_detail_page_info", so_allocation_detail_page_info)  # so查看详情接口
    def test_so_allocation_detail_page_info(self, so_allocation_detail_page_info, get_token):
        result = Request().send(
            url=so_allocation_detail_page_info["url"] + str(read_yaml(Path.out_order_middle_path, "so_id", "data")),
            method=so_allocation_detail_page_info["method"],
            headers=get_token)
        logger.info(so_allocation_detail_page_info['title'], result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("so列表查询接口")
    @pytest.mark.order(8)
    @pytest.mark.parametrize("so_page_info", so_page_info)  # so列表查询接口
    def test_so_page_info(self, so_page_info, get_token):
        result = Request().send(
            url=so_page_info["url"],
            method=so_page_info["method"],
            data=so_page_info["data"],
            headers=get_token)
        logger.info(so_page_info['title'], result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("so查看接口")
    @pytest.mark.order(9)
    @pytest.mark.parametrize("so_detail_info", so_detail_info)  # so查看接口
    def test_so_page_info(self, so_detail_info, get_token):
        result = Request().send(
            url=so_detail_info["url"] + str(read_yaml(Path.out_order_middle_path, "so_id", "data")),
            method=so_detail_info["method"],
            headers=get_token)
        logger.info(so_detail_info['title'], result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'
