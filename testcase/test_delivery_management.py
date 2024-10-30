import pytest
from config.path import *
from utils.get_yaml_data import *
from utils.requests_util import Request
from utils.log import logger
from utils.other_utils import *
from utils.mysql_util import CommonDatabase
import requests
import allure


class TestDeliveryManagement:
    delivery_arrange_page_info = read_yaml(Path.delivery_management_path, "delivery_arrange_page_info")
    create_delivery_loading_order = read_yaml(Path.delivery_management_path, "create_delivery_loading_order")
    car_delivery_page_info = read_yaml(Path.delivery_management_path, "car_delivery_page_info")
    append_order_car = read_yaml(Path.delivery_management_path, "append_order_car")
    car_delivery_down_page_info = read_yaml(Path.delivery_management_path, "car_delivery_down_page_info")
    car_delivery_down_detail_info = read_yaml(Path.delivery_management_path, "car_delivery_down_detail_info")
    car_driver_select = read_yaml(Path.delivery_management_path, "car_driver_select")
    delivery_order_down = read_yaml(Path.delivery_management_path, "delivery_order_down")
    delivery_check_page_info = read_yaml(Path.delivery_management_path, "delivery_check_page_info")
    delivery_check_detail_info = read_yaml(Path.delivery_management_path, "delivery_check_detail_info")
    delivery_order_print = read_yaml(Path.delivery_management_path, "delivery_order_print")
    delivery_drug_print = read_yaml(Path.delivery_management_path, "delivery_drug_print")
    delivery_cold_print = read_yaml(Path.delivery_management_path, "delivery_cold_print")
    delivery_summary_print = read_yaml(Path.delivery_management_path, "delivery_summary_print")
    delivery_check = read_yaml(Path.delivery_management_path, "delivery_check")
    delivery_get_back_page_info = read_yaml(Path.delivery_management_path, "delivery_get_back_page_info")
    delivery_get_back_detail_info = read_yaml(Path.delivery_management_path, "delivery_get_back_detail_info")

    @allure.title("配送排车列表查询接口")
    @pytest.mark.parametrize("delivery_arrange_page_info",
                             delivery_arrange_page_info)  # 配送排车列表查询接口
    def test_delivery_arrange_page_info(self, delivery_arrange_page_info, get_token):
        result = Request().send(url=delivery_arrange_page_info["url"],
                                method=delivery_arrange_page_info["method"],
                                data=delivery_arrange_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
        assert result['body']['obj'] is not None
        write_yaml(Path.delivery_middle_path, "so_id", "data", result['body']['obj'][0]['key'], dict_key=None)

    @allure.title("配送排车装车单创建接口")
    @pytest.mark.parametrize("create_delivery_loading_order",
                             create_delivery_loading_order)  # 配送排车装车单创建接口
    def test_create_delivery_loading_order(self, create_delivery_loading_order, get_token):
        result = Request().send(url=create_delivery_loading_order["url"],
                                method=create_delivery_loading_order["method"],
                                data={},
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送排车列表查询接口")
    @pytest.mark.parametrize("car_delivery_page_info",
                             car_delivery_page_info)  # 配送排车列表查询接口
    def test_car_delivery_page_info(self, car_delivery_page_info, get_token):
        result = Request().send(url=car_delivery_page_info["url"],
                                method=car_delivery_page_info["method"],
                                data=car_delivery_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
        write_yaml(Path.delivery_middle_path, "car_id", "data", result['body']['obj'][0]['key'], dict_key=None)

    @allure.title("配送装车接口")
    @pytest.mark.parametrize("append_order_car",
                             append_order_car)  # 配送装车接口
    def test_append_order_car(self, append_order_car, get_token):
        result = Request().send(
            url=append_order_car["url"] + str(read_yaml(Path.delivery_middle_path, "car_id", "data")),
            method=append_order_car["method"],
            data=[f'{read_yaml(Path.delivery_middle_path, "so_id", "data")}'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送装车下发列表查询接口")
    @pytest.mark.parametrize("car_delivery_down_page_info",
                             car_delivery_down_page_info)  # 配送装车下发列表查询接口
    def test_car_delivery_down_page_info(self, car_delivery_down_page_info, get_token):
        result = Request().send(
            url=car_delivery_down_page_info["url"],
            method=car_delivery_down_page_info["method"],
            data=car_delivery_down_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送装车下发列表详情查询接口")
    @pytest.mark.parametrize("car_delivery_down_detail_info",
                             car_delivery_down_detail_info)  # 配送装车下发列表详情查询接口
    def test_car_delivery_down_detail_info(self, car_delivery_down_detail_info, get_token):
        car_delivery_down_detail_info['data'][
            'loadingOrderId'] = f"{read_yaml(Path.delivery_middle_path, 'car_id', 'data')}"
        result = Request().send(
            url=car_delivery_down_detail_info["url"],
            method=car_delivery_down_detail_info["method"],
            data=car_delivery_down_detail_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送装车下发司机选择接口")
    @pytest.mark.parametrize("car_driver_select",
                             car_driver_select)  # 配送装车下发司机选择接口
    def test_car_driver_select(self, car_driver_select, get_token):
        car_driver_select['data'][
            'id'] = f"{read_yaml(Path.delivery_middle_path, 'car_id', 'data')}"
        car_driver_select['data'][
            'loadingOrderDispatchUpdateReq']['id'] = f"{read_yaml(Path.delivery_middle_path, 'car_id', 'data')}"
        result = Request().send(
            url=car_driver_select["url"],
            method=car_driver_select["method"],
            data=car_driver_select['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送装车单下发接口")
    @pytest.mark.parametrize("delivery_order_down",
                             delivery_order_down)  # 配送装车单下发接口
    def test_delivery_order_down(self, delivery_order_down, get_token):
        result = Request().send(
            url=delivery_order_down["url"],
            method=delivery_order_down["method"],
            data=[f"{read_yaml(Path.delivery_middle_path, 'car_id', 'data')}"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送装车确认列表查询接口")
    @pytest.mark.parametrize("delivery_check_page_info",
                             delivery_check_page_info)  # 配送装车确认列表查询接口
    def test_delivery_check_page_info(self, delivery_check_page_info, get_token):
        result = Request().send(
            url=delivery_check_page_info["url"],
            method=delivery_check_page_info["method"],
            data=delivery_check_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送装车确认详情明细查询接口")
    @pytest.mark.parametrize("delivery_check_detail_info",
                             delivery_check_detail_info)  # 配送装车确认详情明细查询接口
    def test_delivery_check_detail_info(self, delivery_check_detail_info, get_token):
        delivery_check_detail_info['data'][
            'loadingOrderId'] = f"{read_yaml(Path.delivery_middle_path, 'car_id', 'data')}"
        result = Request().send(
            url=delivery_check_detail_info["url"],
            method=delivery_check_detail_info["method"],
            data=delivery_check_detail_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送装车单打印接口")
    @pytest.mark.parametrize("delivery_order_print",
                             delivery_order_print)  # 配送装车单打印接口
    def test_delivery_order_print(self, delivery_order_print, get_token):
        delivery_order_print['data'][
            'loadingOrderIds'] = [f"{read_yaml(Path.delivery_middle_path, 'car_id', 'data')}"]
        result = Request().send(
            url=delivery_order_print["url"],
            method=delivery_order_print["method"],
            data=delivery_order_print['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送特管药打印接口")
    @pytest.mark.parametrize("delivery_drug_print",
                             delivery_drug_print)  # 配送特管药打印接口
    def test_delivery_drug_print(self, delivery_drug_print, get_token):
        delivery_drug_print['data'][
            'loadingOrderIds'] = [f"{read_yaml(Path.delivery_middle_path, 'car_id', 'data')}"]
        result = Request().send(
            url=delivery_drug_print["url"],
            method=delivery_drug_print["method"],
            data=delivery_drug_print['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送装车冷链装车单打印")
    @pytest.mark.parametrize("delivery_cold_print",
                             delivery_cold_print)  # 配送装车冷链装车单打印
    def test_delivery_cold_print(self, delivery_cold_print, get_token):
        delivery_cold_print['data'][
            'loadingOrderIds'] = [f"{read_yaml(Path.delivery_middle_path, 'car_id', 'data')}"]
        result = Request().send(
            url=delivery_cold_print["url"],
            method=delivery_cold_print["method"],
            data=delivery_cold_print['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送装车单汇总单打印")
    @pytest.mark.parametrize("delivery_summary_print",
                             delivery_summary_print)  # 配送装车单汇总单打印
    def test_delivery_summary_print(self, delivery_summary_print, get_token):
        delivery_summary_print['data'][
            'loadingOrderIds'] = [f"{read_yaml(Path.delivery_middle_path, 'car_id', 'data')}"]
        result = Request().send(
            url=delivery_summary_print["url"],
            method=delivery_summary_print["method"],
            data=delivery_summary_print['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送装车单直接确认接口")
    @pytest.mark.parametrize("delivery_check",
                             delivery_check)  # 配送装车单直接确认接口
    def test_delivery_check(self, delivery_check, get_token):
        result = Request().send(
            url=delivery_check["url"],
            method=delivery_check["method"],
            data=[f"{read_yaml(Path.delivery_middle_path, 'car_id', 'data')}"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送装车单配送返回列表查询接口")
    @pytest.mark.parametrize("delivery_get_back_page_info",
                             delivery_get_back_page_info)  # 配送装车单直接确认接口
    def test_delivery_get_back_page_info(self, delivery_get_back_page_info, get_token):
        result = Request().send(
            url=delivery_get_back_page_info["url"],
            method=delivery_get_back_page_info["method"],
            data=delivery_get_back_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("配送返回装车单详情查询接口")
    @pytest.mark.parametrize("delivery_get_back_detail_info",
                             delivery_get_back_detail_info)  # 配送返回装车单详情查询接口
    def test_delivery_get_back_detail_info(self, delivery_get_back_detail_info, get_token):
        delivery_get_back_detail_info['data'][
            'loadingOrderId'] = f"{read_yaml(Path.delivery_middle_path, 'car_id', 'data')}"
        result = Request().send(
            url=delivery_get_back_detail_info["url"],
            method=delivery_get_back_detail_info["method"],
            data=delivery_get_back_detail_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
