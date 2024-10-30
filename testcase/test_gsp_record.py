import pytest
from config.path import *
from utils.get_yaml_data import *
from utils.requests_util import Request
from utils.log import logger
from utils.other_utils import *
from utils.mysql_util import CommonDatabase
import requests
import allure


class TestGspRecord:
    select_resave_record_page_info = read_yaml(Path.gsp_management_path, "select_resave_record_page_info")
    select_check_record_page_info = read_yaml(Path.gsp_management_path, "select_check_record_page_info")
    select_in_order_record_page_info = read_yaml(Path.gsp_management_path, "select_in_order_record_page_info")
    select_out_order_fh_record_page_info = read_yaml(Path.gsp_management_path, "select_out_order_fh_record_page_info")
    select_check_yh_record_page_info = read_yaml(Path.gsp_management_path, "select_check_yh_record_page_info")
    select_yh_record_page_info = read_yaml(Path.gsp_management_path, "select_yh_record_page_info")
    select_recheck_record_page_info = read_yaml(Path.gsp_management_path, "select_recheck_record_page_info")
    select_bhg_report_record_page_info = read_yaml(Path.gsp_management_path, "select_bhg_report_record_page_info")
    select_bhg_record_page_info = read_yaml(Path.gsp_management_path, "select_bhg_record_page_info")
    select_bhg_destroy_record_page_info = read_yaml(Path.gsp_management_path, "select_bhg_destroy_record_page_info")
    select_refused_record_page_info = read_yaml(Path.gsp_management_path, "select_refused_record_page_info")
    select_jxq_cx_record_page_info = read_yaml(Path.gsp_management_path, "select_jxq_cx_record_page_info")
    select_zx_cx_record_page_info = read_yaml(Path.gsp_management_path, "select_zx_cx_record_page_info")

    @allure.title("产品收货查询接口")
    @pytest.mark.parametrize("select_resave_record_page_info",
                             select_resave_record_page_info)  # 产品收货查询接口
    def test_select_resave_record_page_info(self, select_resave_record_page_info, get_token):
        result = Request().send(url=select_resave_record_page_info["url"],
                                method=select_resave_record_page_info["method"],
                                data=select_resave_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0

    @allure.title("产品验收记录查询接口")
    @pytest.mark.parametrize("select_check_record_page_info",
                             select_check_record_page_info)  # 产品验收记录查询接口
    def test_select_check_record_page_info(self, select_check_record_page_info, get_token):
        result = Request().send(url=select_check_record_page_info["url"],
                                method=select_check_record_page_info["method"],
                                data=select_check_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0

    @allure.title("产品入库记录查询接口")
    @pytest.mark.parametrize("select_in_order_record_page_info",
                             select_in_order_record_page_info)  # 产品入库记录查询接口
    def test_select_in_order_record_page_info(self, select_in_order_record_page_info, get_token):
        result = Request().send(url=select_in_order_record_page_info["url"],
                                method=select_in_order_record_page_info["method"],
                                data=select_in_order_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0

    @allure.title("产品出库复核记录查询接口")
    @pytest.mark.parametrize("select_out_order_fh_record_page_info",
                             select_out_order_fh_record_page_info)  # 产品出库复核记录查询接口
    def test_select_out_order_fh_record_page_info(self, select_out_order_fh_record_page_info, get_token):
        result = Request().send(url=select_out_order_fh_record_page_info["url"],
                                method=select_out_order_fh_record_page_info["method"],
                                data=select_out_order_fh_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0

    @allure.title("产品养护确认记录查询接口")
    @pytest.mark.parametrize("select_check_yh_record_page_info",
                             select_check_yh_record_page_info)  # 产品养护确认记录查询接口
    def test_select_check_yh_record_page_info(self, select_check_yh_record_page_info, get_token):
        result = Request().send(url=select_check_yh_record_page_info["url"],
                                method=select_check_yh_record_page_info["method"],
                                data=select_check_yh_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0

    @allure.title("产品养护记录查询接口")
    @pytest.mark.parametrize("select_yh_record_page_info",
                             select_yh_record_page_info)  # 产品养护记录查询接口
    def test_select_yh_record_page_info(self, select_yh_record_page_info, get_token):
        result = Request().send(url=select_yh_record_page_info["url"],
                                method=select_yh_record_page_info["method"],
                                data=select_yh_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0

    @allure.title("产品复检记录查询接口")
    @pytest.mark.parametrize("select_recheck_record_page_info",
                             select_recheck_record_page_info)  # 产品复检记录查询接口
    def test_select_recheck_record_page_info(self, select_recheck_record_page_info, get_token):
        result = Request().send(url=select_recheck_record_page_info["url"],
                                method=select_recheck_record_page_info["method"],
                                data=select_recheck_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0

    @allure.title("不合格产品报损记录查询接口")
    @pytest.mark.parametrize("select_bhg_report_record_page_info",
                             select_bhg_report_record_page_info)  # 不合格产品报损记录查询接口
    def test_select_bhg_report_record_page_info(self, select_bhg_report_record_page_info, get_token):
        result = Request().send(url=select_bhg_report_record_page_info["url"],
                                method=select_bhg_report_record_page_info["method"],
                                data=select_bhg_report_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0

    @allure.title("不合格产品记录查询接口")
    @pytest.mark.parametrize("select_bhg_record_page_info",
                             select_bhg_record_page_info)  # 不合格产品记录查询接口
    def test_select_bhg_record_page_info(self, select_bhg_record_page_info, get_token):
        result = Request().send(url=select_bhg_record_page_info["url"],
                                method=select_bhg_record_page_info["method"],
                                data=select_bhg_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0

    @allure.title("不合格产品销毁记录查询接口")
    @pytest.mark.parametrize("select_bhg_destroy_record_page_info",
                             select_bhg_destroy_record_page_info)  # 不合格产品销毁记录查询接口
    def test_select_bhg_destroy_record_page_info(self, select_bhg_destroy_record_page_info, get_token):
        result = Request().send(url=select_bhg_destroy_record_page_info["url"],
                                method=select_bhg_destroy_record_page_info["method"],
                                data=select_bhg_destroy_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0

    @allure.title("产品拒收记录查询接口")
    @pytest.mark.parametrize("select_refused_record_page_info",
                             select_refused_record_page_info)  # 产品拒收记录查询接口
    def test_select_refused_record_page_info(self, select_refused_record_page_info, get_token):
        result = Request().send(url=select_refused_record_page_info["url"],
                                method=select_refused_record_page_info["method"],
                                data=select_refused_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0

    @allure.title("产品近效期催销记录")
    @pytest.mark.parametrize("select_jxq_cx_record_page_info",
                             select_jxq_cx_record_page_info)  # 产品近效期催销记录
    def test_select_jxq_cx_record_page_info(self, select_jxq_cx_record_page_info, get_token):
        result = Request().send(url=select_jxq_cx_record_page_info["url"],
                                method=select_jxq_cx_record_page_info["method"],
                                data=select_jxq_cx_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0

    @allure.title("产品滞销催销记录")
    @pytest.mark.parametrize("select_zx_cx_record_page_info",
                             select_zx_cx_record_page_info)  # 产品滞销催销记录
    def test_select_zx_cx_record_page_info(self, select_zx_cx_record_page_info, get_token):
        result = Request().send(url=select_zx_cx_record_page_info["url"],
                                method=select_zx_cx_record_page_info["method"],
                                data=select_zx_cx_record_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["total"] > 0
