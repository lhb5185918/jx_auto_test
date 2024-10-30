import pytest
from config.path import *
from utils.get_yaml_data import *
from utils.requests_util import Request
from utils.log import logger
from utils.other_utils import *
from utils.mysql_util import CommonDatabase
import requests
import allure


class TestWarehouseInside:
    location_forms_select = read_yaml(Path.report_forms_path, "location_forms_select")
    inventory_container_forms_select = read_yaml(Path.report_forms_path, "inventory_container_forms_select")
    inventory_total_forms_select = read_yaml(Path.report_forms_path, "inventory_total_forms_select")
    inventory_detail_forms_select = read_yaml(Path.report_forms_path, "inventory_detail_forms_select")
    inventory_sale_forms_select = read_yaml(Path.report_forms_path, "inventory_sale_forms_select")
    inventory_age_forms_select = read_yaml(Path.report_forms_path, "inventory_age_forms_select")
    inventory_wait_allocation_forms_select = read_yaml(Path.report_forms_path, "inventory_wait_allocation_forms_select")
    inventory_status_change_forms_select = read_yaml(Path.report_forms_path, "inventory_status_change_forms_select")
    in_order_detail_forms_select = read_yaml(Path.report_forms_path, "in_order_detail_forms_select")
    in_order_resave_detail_forms_select = read_yaml(Path.report_forms_path, "in_order_resave_detail_forms_select")
    in_order_check_detail_forms_select = read_yaml(Path.report_forms_path, "in_order_check_detail_forms_select")
    in_order_put_shelf_detail_forms_select = read_yaml(Path.report_forms_path, "in_order_put_shelf_detail_forms_select")
    in_order_order_detail_forms_select = read_yaml(Path.report_forms_path, "in_order_order_detail_forms_select")
    in_order_work_detail_forms_select = read_yaml(Path.report_forms_path, "in_order_work_detail_forms_select")
    in_order_monitor_detail_forms_select = read_yaml(Path.report_forms_path, "in_order_monitor_detail_forms_select")
    warehouse_inside_hc_forms_select = read_yaml(Path.report_forms_path, "warehouse_inside_hc_forms_select")
    warehouse_inside_machining_forms_select = read_yaml(Path.report_forms_path,
                                                        "warehouse_inside_machining_forms_select")
    warehouse_inside_product_change_forms_select = read_yaml(Path.report_forms_path,
                                                             "warehouse_inside_product_change_forms_select")
    warehouse_inside_replenish_forms_select = read_yaml(Path.report_forms_path,
                                                        "warehouse_inside_replenish_forms_select")
    warehouse_product_batch_forms_select = read_yaml(Path.report_forms_path, "warehouse_product_batch_forms_select")
    warehouse_lock_forms_select = read_yaml(Path.report_forms_path, "warehouse_lock_forms_select")
    warehouse_un_lock_forms_select = read_yaml(Path.report_forms_path, "warehouse_un_lock_forms_select")
    warehouse_move_forms_select = read_yaml(Path.report_forms_path, "warehouse_move_forms_select")
    warehouse_move_location_forms_select = read_yaml(Path.report_forms_path, "warehouse_move_location_forms_select")
    warehouse_bhg_forms_select = read_yaml(Path.report_forms_path, "warehouse_bhg_forms_select")
    warehouse_stock_taking_forms_select = read_yaml(Path.report_forms_path, "warehouse_stock_taking_forms_select")
    out_order_allocation_detail_forms_select = read_yaml(Path.report_forms_path,
                                                         "out_order_allocation_detail_forms_select")
    out_order_detail_forms_select = read_yaml(Path.report_forms_path, "out_order_detail_forms_select")
    out_order_cancel_forms_select = read_yaml(Path.report_forms_path, "out_order_cancel_forms_select")
    out_order_pick_detail_forms_select = read_yaml(Path.report_forms_path, "out_order_pick_detail_forms_select")
    out_order_heavy_detail_forms_select = read_yaml(Path.report_forms_path, "out_order_heavy_detail_forms_select")
    out_order_review_process_detail_forms_select = read_yaml(Path.report_forms_path,
                                                             "out_order_review_process_detail_forms_select")
    out_order_picking_process_detail_forms_select = read_yaml(Path.report_forms_path,
                                                              "out_order_picking_process_detail_forms_select")
    out_order_work_detail_forms_select = read_yaml(Path.report_forms_path, "out_order_work_detail_forms_select")
    out_order_move_zcq_detail_forms_select = read_yaml(Path.report_forms_path, "out_order_move_zcq_detail_forms_select")
    out_order_frequency_detail_forms_select = read_yaml(Path.report_forms_path,
                                                        "out_order_frequency_detail_forms_select")
    out_order_statistic_detail_forms_select = read_yaml(Path.report_forms_path,
                                                        "out_order_statistic_detail_forms_select")
    out_order_monitor_detail_forms_select = read_yaml(Path.report_forms_path, "out_order_monitor_detail_forms_select")
    out_order_instruction_detail_forms_select = read_yaml(Path.report_forms_path,
                                                          "out_order_instruction_detail_forms_select")
    delivery_cars_detail_forms_select = read_yaml(Path.report_forms_path, "delivery_cars_detail_forms_select")
    delivery_logistics_detail_forms_select = read_yaml(Path.report_forms_path, "delivery_logistics_detail_forms_select")
    delivery_history_detail_forms_select = read_yaml(Path.report_forms_path, "delivery_history_detail_forms_select")
    consignment_history_detail_forms_select = read_yaml(Path.report_forms_path,
                                                        "consignment_history_detail_forms_select")
    get_car_wait_order_detail_forms_select = read_yaml(Path.report_forms_path, "get_car_wait_order_detail_forms_select")
    delivery_forms_select = read_yaml(Path.report_forms_path, "delivery_forms_select")
    consignment_forms_select = read_yaml(Path.report_forms_path, "consignment_forms_select")
    work_statistics_detail_forms_select = read_yaml(Path.report_forms_path, "work_statistics_detail_forms_select")
    b2b_relation_detail_forms_select = read_yaml(Path.report_forms_path, "b2b_relation_detail_forms_select")

    @allure.title("货位快捷查询接口")
    @pytest.mark.parametrize("location_forms_select", location_forms_select)  # 货位快捷查询接口
    def test_location_forms_select(self, location_forms_select, get_token):
        result = Request().send(url=location_forms_select["url"], method=location_forms_select["method"],
                                data=location_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("库存容器查询接口")
    @pytest.mark.parametrize("inventory_container_forms_select", inventory_container_forms_select)  # 库存容器查询接口
    def test_inventory_container_forms_select(self, inventory_container_forms_select, get_token):
        result = Request().send(url=inventory_container_forms_select["url"],
                                method=inventory_container_forms_select["method"],
                                data=inventory_container_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("库存总账查询接口")
    @pytest.mark.parametrize("inventory_total_forms_select", inventory_total_forms_select)  # 库存总账查询接口
    def test_inventory_total_forms_select(self, inventory_total_forms_select, get_token):
        result = Request().send(url=inventory_total_forms_select["url"],
                                method=inventory_total_forms_select["method"],
                                data=inventory_total_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("库存明细查询接口")
    @pytest.mark.parametrize("inventory_detail_forms_select", inventory_detail_forms_select)  # 库存明细查询接口
    def test_inventory_detail_forms_select(self, inventory_detail_forms_select, get_token):
        result = Request().send(url=inventory_detail_forms_select["url"],
                                method=inventory_detail_forms_select["method"],
                                data=inventory_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("库存交易流水查询接口")
    @pytest.mark.parametrize("inventory_sale_forms_select", inventory_sale_forms_select)  # 库存交易流水查询接口
    def test_inventory_sale_forms_select(self, inventory_sale_forms_select, get_token):
        result = Request().send(url=inventory_sale_forms_select["url"],
                                method=inventory_sale_forms_select["method"],
                                data=inventory_sale_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("库龄分析查询接口")
    @pytest.mark.parametrize("inventory_age_forms_select", inventory_age_forms_select)  # 库龄分析查询接口
    def test_inventory_age_forms_select(self, inventory_age_forms_select, get_token):
        result = Request().send(url=inventory_age_forms_select["url"],
                                method=inventory_age_forms_select["method"],
                                data=inventory_age_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("带扣减库存查询接口")
    @pytest.mark.parametrize("inventory_wait_allocation_forms_select",
                             inventory_wait_allocation_forms_select)  # 带扣减库存查询接口
    def test_inventory_wait_allocation_forms_select(self, inventory_wait_allocation_forms_select, get_token):
        result = Request().send(url=inventory_wait_allocation_forms_select["url"],
                                method=inventory_wait_allocation_forms_select["method"],
                                data=inventory_wait_allocation_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("库存状态变更接口")
    @pytest.mark.parametrize("inventory_status_change_forms_select",
                             inventory_status_change_forms_select)  # 库存状态变更接口
    def test_inventory_status_change_forms_select(self, inventory_status_change_forms_select, get_token):
        result = Request().send(url=inventory_status_change_forms_select["url"],
                                method=inventory_status_change_forms_select["method"],
                                data=inventory_status_change_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("入库订单明细查询接口")
    @pytest.mark.parametrize("in_order_detail_forms_select",
                             in_order_detail_forms_select)  # 入库订单明细查询接口
    def test_in_order_detail_forms_select(self, in_order_detail_forms_select, get_token):
        result = Request().send(url=in_order_detail_forms_select["url"],
                                method=in_order_detail_forms_select["method"],
                                data=in_order_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("入库收货明细表查询接口")
    @pytest.mark.parametrize("in_order_resave_detail_forms_select",
                             in_order_resave_detail_forms_select)  # 入库收货明细表查询接口
    def test_in_order_resave_detail_forms_select(self, in_order_resave_detail_forms_select, get_token):
        result = Request().send(url=in_order_resave_detail_forms_select["url"],
                                method=in_order_resave_detail_forms_select["method"],
                                data=in_order_resave_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("入库验收明细表查询接口")
    @pytest.mark.parametrize("in_order_check_detail_forms_select",
                             in_order_check_detail_forms_select)  # 入库验收明细表查询接口
    def test_in_order_check_detail_forms_select(self, in_order_check_detail_forms_select, get_token):
        result = Request().send(url=in_order_check_detail_forms_select["url"],
                                method=in_order_check_detail_forms_select["method"],
                                data=in_order_check_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("入库上架明细表查询接口")
    @pytest.mark.parametrize("in_order_put_shelf_detail_forms_select",
                             in_order_put_shelf_detail_forms_select)  # 入库上架明细表查询接口
    def test_in_order_put_shelf_detail_forms_select(self, in_order_put_shelf_detail_forms_select, get_token):
        result = Request().send(url=in_order_put_shelf_detail_forms_select["url"],
                                method=in_order_put_shelf_detail_forms_select["method"],
                                data=in_order_put_shelf_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("入库单明细表查询接口")
    @pytest.mark.parametrize("in_order_order_detail_forms_select",
                             in_order_order_detail_forms_select)  # 入库单明细表查询接口
    def test_in_order_order_detail_forms_select(self, in_order_order_detail_forms_select, get_token):
        result = Request().send(url=in_order_order_detail_forms_select["url"],
                                method=in_order_order_detail_forms_select["method"],
                                data=in_order_order_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("入库订单作业汇总表查询接口")
    @pytest.mark.parametrize("in_order_work_detail_forms_select",
                             in_order_work_detail_forms_select)  # 入库订单作业汇总表查询接口
    def test_in_order_work_detail_forms_select(self, in_order_work_detail_forms_select, get_token):
        result = Request().send(url=in_order_work_detail_forms_select["url"],
                                method=in_order_work_detail_forms_select["method"],
                                data=in_order_work_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("入库监控报表查询接口")
    @pytest.mark.parametrize("in_order_monitor_detail_forms_select",
                             in_order_monitor_detail_forms_select)  # 入库监控报表查询接口
    def test_in_order_monitor_detail_forms_select(self, in_order_monitor_detail_forms_select, get_token):
        result = Request().send(url=in_order_monitor_detail_forms_select["url"],
                                method=in_order_monitor_detail_forms_select["method"],
                                data=in_order_monitor_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("耗材库存记录查询接口")
    @pytest.mark.parametrize("warehouse_inside_hc_forms_select",
                             warehouse_inside_hc_forms_select)  # 耗材库存记录查询接口
    def test_warehouse_inside_hc_forms_select(self, warehouse_inside_hc_forms_select, get_token):
        result = Request().send(url=warehouse_inside_hc_forms_select["url"],
                                method=warehouse_inside_hc_forms_select["method"],
                                data=warehouse_inside_hc_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("加工明细记录查询接口")
    @pytest.mark.parametrize("warehouse_inside_machining_forms_select",
                             warehouse_inside_machining_forms_select)  # 加工明细记录查询接口
    def test_warehouse_inside_machining_forms_select(self, warehouse_inside_machining_forms_select, get_token):
        result = Request().send(url=warehouse_inside_machining_forms_select["url"],
                                method=warehouse_inside_machining_forms_select["method"],
                                data=warehouse_inside_machining_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("货转单明细记录查询接口")
    @pytest.mark.parametrize("warehouse_inside_product_change_forms_select",
                             warehouse_inside_product_change_forms_select)  # 货转单明细记录查询接口
    def test_warehouse_inside_product_change_forms_select(self, warehouse_inside_product_change_forms_select,
                                                          get_token):
        result = Request().send(url=warehouse_inside_product_change_forms_select["url"],
                                method=warehouse_inside_product_change_forms_select["method"],
                                data=warehouse_inside_product_change_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("补货报表查询接口")
    @pytest.mark.parametrize("warehouse_inside_replenish_forms_select",
                             warehouse_inside_replenish_forms_select)  # 补货报表查询接口
    def test_warehouse_inside_replenish_forms_select(self, warehouse_inside_replenish_forms_select,
                                                     get_token):
        result = Request().send(url=warehouse_inside_replenish_forms_select["url"],
                                method=warehouse_inside_replenish_forms_select["method"],
                                data=warehouse_inside_replenish_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("批次调整记录报表查询接口")
    @pytest.mark.parametrize("warehouse_product_batch_forms_select",
                             warehouse_product_batch_forms_select)  # 批次调整记录报表查询接口
    def test_warehouse_product_batch_forms_select(self, warehouse_product_batch_forms_select,
                                                  get_token):
        result = Request().send(url=warehouse_product_batch_forms_select["url"],
                                method=warehouse_product_batch_forms_select["method"],
                                data=warehouse_product_batch_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("库存锁定记录查询接口")
    @pytest.mark.parametrize("warehouse_lock_forms_select",
                             warehouse_lock_forms_select)  # 库存锁定记录查询接口
    def test_warehouse_lock_forms_select(self, warehouse_lock_forms_select,
                                         get_token):
        result = Request().send(url=warehouse_lock_forms_select["url"],
                                method=warehouse_lock_forms_select["method"],
                                data=warehouse_lock_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("库存解锁记录查询接口")
    @pytest.mark.parametrize("warehouse_un_lock_forms_select",
                             warehouse_un_lock_forms_select)  # 库存解锁记录查询接口
    def test_warehouse_un_lock_forms_select(self, warehouse_un_lock_forms_select,
                                            get_token):
        result = Request().send(url=warehouse_un_lock_forms_select["url"],
                                method=warehouse_un_lock_forms_select["method"],
                                data=warehouse_un_lock_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("移库明细查询接口")
    @pytest.mark.parametrize("warehouse_move_forms_select",
                             warehouse_move_forms_select)  # 移库明细查询接口
    def test_warehouse_move_forms_select(self, warehouse_move_forms_select,
                                         get_token):
        result = Request().send(url=warehouse_move_forms_select["url"],
                                method=warehouse_move_forms_select["method"],
                                data=warehouse_move_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("移库明细查询接口")
    @pytest.mark.parametrize("warehouse_move_location_forms_select",
                             warehouse_move_location_forms_select)  # 移库明细查询接口
    def test_warehouse_move_location_forms_select(self, warehouse_move_location_forms_select,
                                                  get_token):
        result = Request().send(url=warehouse_move_location_forms_select["url"],
                                method=warehouse_move_location_forms_select["method"],
                                data=warehouse_move_location_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("不合格产品查询接口")
    @pytest.mark.parametrize("warehouse_bhg_forms_select",
                             warehouse_bhg_forms_select)  # 不合格产品查询接口
    def test_warehouse_bhg_forms_select(self, warehouse_bhg_forms_select,
                                        get_token):
        result = Request().send(url=warehouse_bhg_forms_select["url"],
                                method=warehouse_bhg_forms_select["method"],
                                data=warehouse_bhg_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("盘盈盘亏列表查询接口")
    @pytest.mark.parametrize("warehouse_stock_taking_forms_select",
                             warehouse_stock_taking_forms_select)  # 盘盈盘亏列表查询接口
    def test_warehouse_stock_taking_forms_select(self, warehouse_stock_taking_forms_select,
                                                 get_token):
        result = Request().send(url=warehouse_stock_taking_forms_select["url"],
                                method=warehouse_stock_taking_forms_select["method"],
                                data=warehouse_stock_taking_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("出库订单分配明细查询接口")
    @pytest.mark.parametrize("out_order_allocation_detail_forms_select",
                             out_order_allocation_detail_forms_select)  # 出库订单分配明细查询接口
    def test_out_order_allocation_detail_forms_select(self, out_order_allocation_detail_forms_select,
                                                      get_token):
        result = Request().send(url=out_order_allocation_detail_forms_select["url"],
                                method=out_order_allocation_detail_forms_select["method"],
                                data=out_order_allocation_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("出库订单明细查询接口")
    @pytest.mark.parametrize("out_order_detail_forms_select",
                             out_order_detail_forms_select)  # 出库订单明细查询接口
    def test_out_order_detail_forms_select(self, out_order_detail_forms_select,
                                           get_token):
        result = Request().send(url=out_order_detail_forms_select["url"],
                                method=out_order_detail_forms_select["method"],
                                data=out_order_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("取消订单明细查询接口")
    @pytest.mark.parametrize("out_order_cancel_forms_select",
                             out_order_cancel_forms_select)  # 取消订单明细查询接口
    def test_out_order_cancel_forms_select(self, out_order_cancel_forms_select,
                                           get_token):
        result = Request().send(url=out_order_cancel_forms_select["url"],
                                method=out_order_cancel_forms_select["method"],
                                data=out_order_cancel_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("拣货明细查询接口")
    @pytest.mark.parametrize("out_order_pick_detail_forms_select",
                             out_order_pick_detail_forms_select)  # 拣货明细查询接口
    def test_out_order_pick_detail_forms_select(self, out_order_pick_detail_forms_select,
                                                get_token):
        result = Request().send(url=out_order_pick_detail_forms_select["url"],
                                method=out_order_pick_detail_forms_select["method"],
                                data=out_order_pick_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("称重明细查询接口")
    @pytest.mark.parametrize("out_order_heavy_detail_forms_select",
                             out_order_heavy_detail_forms_select)  # 称重明细查询接口
    def test_out_order_heavy_detail_forms_select(self, out_order_heavy_detail_forms_select,
                                                 get_token):
        result = Request().send(url=out_order_heavy_detail_forms_select["url"],
                                method=out_order_heavy_detail_forms_select["method"],
                                data=out_order_heavy_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("分拣复核进度查询接口")
    @pytest.mark.parametrize("out_order_review_process_detail_forms_select",
                             out_order_review_process_detail_forms_select)  # 分拣复核进度查询接口
    def test_out_order_review_process_detail_forms_select(self, out_order_review_process_detail_forms_select,
                                                          get_token):
        result = Request().send(url=out_order_review_process_detail_forms_select["url"],
                                method=out_order_review_process_detail_forms_select["method"],
                                data=out_order_review_process_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("拣货进度查询接口")
    @pytest.mark.parametrize("out_order_picking_process_detail_forms_select",
                             out_order_picking_process_detail_forms_select)  # 拣货进度查询接口
    def test_out_order_picking_process_detail_forms_select(self, out_order_picking_process_detail_forms_select,
                                                           get_token):
        result = Request().send(url=out_order_picking_process_detail_forms_select["url"],
                                method=out_order_picking_process_detail_forms_select["method"],
                                data=out_order_picking_process_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("出库作业记录查询接口")
    @pytest.mark.parametrize("out_order_work_detail_forms_select",
                             out_order_work_detail_forms_select)  # 出库作业记录查询接口
    def test_out_order_work_detail_forms_select(self, out_order_work_detail_forms_select,
                                                get_token):
        result = Request().send(url=out_order_work_detail_forms_select["url"],
                                method=out_order_work_detail_forms_select["method"],
                                data=out_order_work_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("暂存区移位记录查询接口")
    @pytest.mark.parametrize("out_order_move_zcq_detail_forms_select",
                             out_order_move_zcq_detail_forms_select)  # 暂存区移位记录查询接口
    def test_out_order_move_zcq_detail_forms_select(self, out_order_move_zcq_detail_forms_select,
                                                    get_token):
        result = Request().send(url=out_order_move_zcq_detail_forms_select["url"],
                                method=out_order_move_zcq_detail_forms_select["method"],
                                data=out_order_move_zcq_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("出库频次查询接口")
    @pytest.mark.parametrize("out_order_frequency_detail_forms_select",
                             out_order_frequency_detail_forms_select)  # 出库频次查询接口
    def test_out_order_frequency_detail_forms_select(self, out_order_frequency_detail_forms_select,
                                                     get_token):
        result = Request().send(url=out_order_frequency_detail_forms_select["url"],
                                method=out_order_frequency_detail_forms_select["method"],
                                data=out_order_frequency_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("发货统计列表查询接口")
    @pytest.mark.parametrize("out_order_statistic_detail_forms_select",
                             out_order_statistic_detail_forms_select)  # 发货统计列表查询接口
    def test_out_order_statistic_detail_forms_select(self, out_order_statistic_detail_forms_select,
                                                     get_token):
        result = Request().send(url=out_order_statistic_detail_forms_select["url"],
                                method=out_order_statistic_detail_forms_select["method"],
                                data=out_order_statistic_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("发货监控列表查询接口")
    @pytest.mark.parametrize("out_order_monitor_detail_forms_select",
                             out_order_monitor_detail_forms_select)  # 发货监控列表查询接口
    def test_out_order_monitor_detail_forms_select(self, out_order_monitor_detail_forms_select,
                                                   get_token):
        result = Request().send(url=out_order_monitor_detail_forms_select["url"],
                                method=out_order_monitor_detail_forms_select["method"],
                                data=out_order_monitor_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("出库指令查询接口")
    @pytest.mark.parametrize("out_order_instruction_detail_forms_select",
                             out_order_instruction_detail_forms_select)  # 出库指令查询接口
    def test_out_order_instruction_detail_forms_select(self, out_order_instruction_detail_forms_select,
                                                       get_token):
        result = Request().send(url=out_order_instruction_detail_forms_select["url"],
                                method=out_order_instruction_detail_forms_select["method"],
                                data=out_order_instruction_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("出车车次查询接口")
    @pytest.mark.parametrize("delivery_cars_detail_forms_select",
                             delivery_cars_detail_forms_select)  # 出车车次查询接口
    def test_delivery_cars_detail_forms_select(self, delivery_cars_detail_forms_select,
                                               get_token):
        result = Request().send(url=delivery_cars_detail_forms_select["url"],
                                method=delivery_cars_detail_forms_select["method"],
                                data=delivery_cars_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("物流单号修改记录")
    @pytest.mark.parametrize("delivery_logistics_detail_forms_select",
                             delivery_logistics_detail_forms_select)  # 物流单号修改记录
    def test_delivery_logistics_detail_forms_select(self, delivery_logistics_detail_forms_select,
                                                    get_token):
        result = Request().send(url=delivery_logistics_detail_forms_select["url"],
                                method=delivery_logistics_detail_forms_select["method"],
                                data=delivery_logistics_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("配送单历史查询")
    @pytest.mark.parametrize("delivery_history_detail_forms_select",
                             delivery_history_detail_forms_select)  # 配送单历史查询
    def test_delivery_history_detail_forms_select(self, delivery_history_detail_forms_select,
                                                  get_token):
        result = Request().send(url=delivery_history_detail_forms_select["url"],
                                method=delivery_history_detail_forms_select["method"],
                                data=delivery_history_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("托运单历史查询")
    @pytest.mark.parametrize("consignment_history_detail_forms_select",
                             consignment_history_detail_forms_select)  # 托运单历史查询
    def test_consignment_history_detail_forms_select(self, consignment_history_detail_forms_select,
                                                     get_token):
        result = Request().send(url=consignment_history_detail_forms_select["url"],
                                method=consignment_history_detail_forms_select["method"],
                                data=consignment_history_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("装车确认滞留单据查询接口")
    @pytest.mark.parametrize("get_car_wait_order_detail_forms_select",
                             get_car_wait_order_detail_forms_select)  # 装车确认滞留单据查询接口
    def test_get_car_wait_order_detail_forms_select(self, get_car_wait_order_detail_forms_select,
                                                    get_token):
        result = Request().send(url=get_car_wait_order_detail_forms_select["url"],
                                method=get_car_wait_order_detail_forms_select["method"],
                                data=get_car_wait_order_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("配送当前与历史查询接口")
    @pytest.mark.parametrize("delivery_forms_select",
                             delivery_forms_select)  # 配送当前与历史查询接口
    def test_delivery_forms_select(self, delivery_forms_select,
                                   get_token):
        result = Request().send(url=delivery_forms_select["url"],
                                method=delivery_forms_select["method"],
                                data=delivery_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("托运当前与历史查询接口")
    @pytest.mark.parametrize("consignment_forms_select",
                             consignment_forms_select)  # 托运当前与历史查询接口
    def test_consignment_forms_select(self, consignment_forms_select,
                                      get_token):
        result = Request().send(url=consignment_forms_select["url"],
                                method=consignment_forms_select["method"],
                                data=consignment_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("作业量统计接口")
    @pytest.mark.parametrize("work_statistics_detail_forms_select",
                             work_statistics_detail_forms_select)  # 作业量统计接口
    def test_work_statistics_detail_forms_select(self, work_statistics_detail_forms_select,
                                                 get_token):
        result = Request().send(url=work_statistics_detail_forms_select["url"],
                                method=work_statistics_detail_forms_select["method"],
                                data=work_statistics_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("b2b委托订单关系查询接口")
    @pytest.mark.parametrize("b2b_relation_detail_forms_select",
                             b2b_relation_detail_forms_select)  # b2b委托订单关系查询接口
    def test_b2b_relation_detail_forms_select(self, b2b_relation_detail_forms_select,
                                              get_token):
        result = Request().send(url=b2b_relation_detail_forms_select["url"],
                                method=b2b_relation_detail_forms_select["method"],
                                data=b2b_relation_detail_forms_select["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None
