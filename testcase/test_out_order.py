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
    so_change_carrier = read_yaml(Path.out_order_data_path, 'so_change_carrier')
    so_print_order = read_yaml(Path.out_order_data_path, 'so_print_order')
    so_print_send_product = read_yaml(Path.out_order_data_path, 'so_print_send_product')
    wave_list_page_info = read_yaml(Path.out_order_data_path, 'wave_list_page_info')
    wave_count_number_info = read_yaml(Path.out_order_data_path, 'wave_count_number_info')
    create_wave_data = read_yaml(Path.out_order_data_path, 'create_wave_data')
    wave_release_page_info = read_yaml(Path.out_order_data_path, 'wave_release_page_info')
    wave_release_detail_info = read_yaml(Path.out_order_data_path, 'wave_release_detail_info')
    wave_staging_update = read_yaml(Path.out_order_data_path, 'wave_staging_update')
    create_release_data = read_yaml(Path.out_order_data_path, 'create_release_data')
    wave_release_list_page_info = read_yaml(Path.out_order_data_path, 'wave_release_list_page_info')
    wave_release_list_detail_info = read_yaml(Path.out_order_data_path, 'wave_release_list_detail_info')
    pick_order_page_info = read_yaml(Path.out_order_data_path, 'pick_order_page_info')
    pick_order_detail_info = read_yaml(Path.out_order_data_path, 'pick_order_detail_info')
    pick_order_print_info = read_yaml(Path.out_order_data_path, 'pick_order_print_info')
    zi_pick_order_assignment = read_yaml(Path.out_order_data_path, 'zi_pick_order_assignment')
    lh_pick_order_assignment = read_yaml(Path.out_order_data_path, 'lh_pick_order_assignment')
    pick_mission_page_info = read_yaml(Path.out_order_data_path, 'pick_mission_page_info')
    pick_mission_detail_info = read_yaml(Path.out_order_data_path, 'pick_order_detail_info')
    pick_mission_fjd_print = read_yaml(Path.out_order_data_path, 'pick_mission_fjd_print')
    pick_mission_detail_print = read_yaml(Path.out_order_data_path, 'pick_mission_detail_print')
    pick_mission_paper_print = read_yaml(Path.out_order_data_path, 'pick_mission_paper_print')
    one_pick_page_info = read_yaml(Path.out_order_data_path, 'one_pick_page_info')
    one_pick_detail_info = read_yaml(Path.out_order_data_path, 'pick_order_detail_info')
    lh_one_pick_data = read_yaml(Path.out_order_data_path, 'lh_one_pick_data')
    zj_one_pick_data = read_yaml(Path.out_order_data_path, 'zj_one_pick_data')
    zj_seeding_page_info = read_yaml(Path.out_order_data_path, 'zj_seeding_page_info')
    zj_seeding_detail_info = read_yaml(Path.out_order_data_path, 'zj_seeding_detail_info')
    zj_seeding_print_info = read_yaml(Path.out_order_data_path, 'zj_seeding_print_info')
    zj_seeding_data = read_yaml(Path.out_order_data_path, 'zj_seeding_data')
    lh_get_seeding_data = read_yaml(Path.out_order_data_path, 'lh_get_seeding_data')
    lh_get_seeding_product_data = read_yaml(Path.out_order_data_path, 'lh_get_seeding_product_data')
    lh_seeding_data = read_yaml(Path.out_order_data_path, 'lh_seeding_data')
    lh_seeding_fjd_data = read_yaml(Path.out_order_data_path, 'lh_seeding_fjd_data')
    lh_seeding_box_label_data = read_yaml(Path.out_order_data_path, 'lh_seeding_box_label_data')
    lh_get_seeding_pick_data = read_yaml(Path.out_order_data_path, 'lh_get_seeding_pick_data')
    lh_get_seeding_fj_data = read_yaml(Path.out_order_data_path, 'lh_get_seeding_fj_data')
    cl_fh_get_mission = read_yaml(Path.out_order_data_path, 'cl_fh_get_mission')
    cl_fh_print_box_no = read_yaml(Path.out_order_data_path, 'cl_fh_print_box_no')
    cl_fh_get_product = read_yaml(Path.out_order_data_path, 'cl_fh_get_product')
    cl_fh_save_data = read_yaml(Path.out_order_data_path, 'cl_fh_save_data')
    cl_fh_down_data = read_yaml(Path.out_order_data_path, 'cl_fh_down_data')
    jh_fh_wait_page_info = read_yaml(Path.out_order_data_path, 'jh_fh_wait_page_info')
    jh_fh_wait_detail_info = read_yaml(Path.out_order_data_path, 'jh_fh_wait_detail_info')
    jh_fh_wait_down = read_yaml(Path.out_order_data_path, 'jh_fh_wait_down')
    jh_fh_page_info = read_yaml(Path.out_order_data_path, 'jh_fh_page_info')
    jh_fh_task = read_yaml(Path.out_order_data_path, 'jh_fh_task')
    jh_fh_detail_info = read_yaml(Path.out_order_data_path, 'jh_fh_detail_info')
    jh_fh_down = read_yaml(Path.out_order_data_path, 'jh_fh_down')
    create_erp_special_data = read_yaml(Path.out_order_data_path, 'create_erp_special_data')
    special_order_page_info = read_yaml(Path.out_order_data_path, 'special_order_page_info')
    special_order_detail_info = read_yaml(Path.out_order_data_path, 'special_order_detail_info')
    special_out_order_data = read_yaml(Path.out_order_data_path, 'special_out_order_data')
    out_oder_print_page_info = read_yaml(Path.out_order_data_path, 'out_oder_print_page_info')
    out_oder_print_detail_info = read_yaml(Path.out_order_data_path, 'out_oder_print_detail_info')
    out_oder_print_sale = read_yaml(Path.out_order_data_path, 'out_oder_print_sale')
    out_oder_print_cold = read_yaml(Path.out_order_data_path, 'out_oder_print_cold')
    out_oder_print_box_no = read_yaml(Path.out_order_data_path, 'out_oder_print_box_no')
    create_toc_out_order = read_yaml(Path.out_order_data_path, 'create_toc_out_order')
    toc_seeding_get_mission = read_yaml(Path.out_order_data_path, 'toc_seeding_get_mission')
    toc_seeding_get_product = read_yaml(Path.out_order_data_path, 'toc_seeding_get_product')
    toc_seeding_data = read_yaml(Path.out_order_data_path, 'toc_seeding_data')
    toc_fh_get_data = read_yaml(Path.out_order_data_path, 'toc_fh_get_data')
    toc_fh_product_data = read_yaml(Path.out_order_data_path, 'toc_fh_product_data')
    toc_fh_down = read_yaml(Path.out_order_data_path, 'toc_fh_down')
    drug_print_page_info = read_yaml(Path.out_order_data_path, 'drug_print_page_info')
    drug_print_report = read_yaml(Path.out_order_data_path, 'drug_print_report')
    with_product_print = read_yaml(Path.out_order_data_path, 'with_product_print')
    invoice_print = read_yaml(Path.out_order_data_path, 'invoice_print')
    drug_prin_detail_info = read_yaml(Path.out_order_data_path, 'drug_prin_detail_info')
    check_drug_print = read_yaml(Path.out_order_data_path, 'check_drug_print')

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
        assert result['code'] == 200 and result["body"]['msg'] == '成功'
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
    @pytest.mark.parametrize("select_out_order_detail_data", select_out_order_detail_data)  # tob_so查看接口
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

    @allure.title("so更换承运商接口")
    @pytest.mark.order(10)
    @pytest.mark.parametrize("so_change_carrier", so_change_carrier)  # so更换承运商接口
    def test_so_change_carrier(self, so_change_carrier, get_token):
        so_change_carrier['data']['ids'] = [f'{read_yaml(Path.out_order_middle_path, "so_id", "data")}']
        so_change_carrier['data']['soNoList'] = [f'{read_yaml(Path.out_order_middle_path, "order_no", "data")}']
        result = Request().send(
            url=so_change_carrier["url"],
            method=so_change_carrier["method"],
            data=so_change_carrier['data'],
            headers=get_token)
        logger.info(so_change_carrier['title'], result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("so打印网店发货单接口")
    @pytest.mark.order(11)
    @pytest.mark.parametrize("so_print_order", so_print_order)  # so打印网店发货单接口
    def test_so_print_order(self, so_print_order, get_token):
        so_print_order['data']['soIdList'] = [f'{read_yaml(Path.out_order_middle_path, "so_id", "data")}']
        result = Request().send(
            url=so_print_order["url"],
            method=so_print_order["method"],
            data=so_print_order['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"][
            'msg'] == "【ZHQCHZ】只支持【采购退货通知单,采购退货通知单(直配),配送单,配送单(直配),调拨出库单,移仓出库单】打印"

    @allure.title("so打印送货单接口")
    @pytest.mark.order(12)
    @pytest.mark.parametrize("so_print_send_product", so_print_send_product)  # so打印送货单接口
    def test_so_print_send_product(self, so_print_send_product, get_token):
        so_print_send_product['data']['soIdList'] = [f'{read_yaml(Path.out_order_middle_path, "so_id", "data")}']
        result = Request().send(
            url=so_print_send_product["url"],
            method=so_print_send_product["method"],
            data=so_print_send_product['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0]['printData'] is not None

    @allure.title("波次预排列表查询接口")
    @pytest.mark.order(13)
    @pytest.mark.parametrize("wave_list_page_info", wave_list_page_info)  # 波次预排列表查询接口
    def test_wave_list_page_info(self, wave_list_page_info, get_token):
        result = Request().send(
            url=wave_list_page_info["url"],
            method=wave_list_page_info["method"],
            data=wave_list_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("波次预排数量统计接口")
    @pytest.mark.order(14)
    @pytest.mark.parametrize("wave_count_number_info", wave_count_number_info)  # 波次预排数量统计接口
    def test_wave_count_number_info(self, wave_count_number_info, get_token):
        result = Request().send(
            url=wave_count_number_info["url"],
            method=wave_count_number_info["method"],
            data=wave_count_number_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("生成波次接口")
    @pytest.mark.order(15)
    @pytest.mark.parametrize("create_wave_data", create_wave_data)  # 生成波次接口
    def test_create_wave_data(self, create_wave_data, get_token):
        create_wave_data['data']['soIdList'] = [f'{read_yaml(Path.out_order_middle_path, "so_id", "data")}']
        result = Request().send(
            url=create_wave_data["url"],
            method=create_wave_data["method"],
            data=create_wave_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("波次下发列表查询接口")
    @pytest.mark.order(16)
    @pytest.mark.parametrize("wave_release_page_info", wave_release_page_info)  # 波次下发列表查询接口
    def test_wave_release_page_info(self, wave_release_page_info, get_token):
        result = Request().send(
            url=wave_release_page_info["url"],
            method=wave_release_page_info["method"],
            data=wave_release_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None
        write_yaml(Path.out_order_middle_path, "wave_id", "data", result["body"]['obj'][0]['key'], dict_key=None)

    @allure.title("波次详情明细查询接口")
    @pytest.mark.order(17)
    @pytest.mark.parametrize("wave_release_detail_info", wave_release_detail_info)  # 波次详情明细查询接口
    def test_wave_release_detail_info(self, wave_release_detail_info, get_token):
        result = Request().send(
            url=wave_release_detail_info["url"] + str(read_yaml(Path.out_order_middle_path, "wave_id", "data")),
            method=wave_release_detail_info["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'
        write_yaml(Path.out_order_middle_path, "wave_dt_id", "data", result["body"]['obj'][0]['key'], dict_key=None)

    @allure.title("波次暂存区设置接口")
    @pytest.mark.order(18)
    @pytest.mark.parametrize("wave_staging_update", wave_staging_update)  # 波次暂存区设置接口
    def test_wave_staging_update(self, wave_staging_update, get_token):
        result = Request().send(
            url=wave_staging_update["url"],
            method=wave_staging_update["method"],
            data=[f'{read_yaml(Path.out_order_middle_path, "wave_dt_id", "data")}'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("波次发布接口")
    @pytest.mark.order(19)
    @pytest.mark.parametrize("create_release_data", create_release_data)  # 波次发布接口
    def test_create_release_data(self, create_release_data, get_token):
        create_release_data['data']['idList'] = [f'{read_yaml(Path.out_order_middle_path, "wave_id", "data")}']
        result = Request().send(
            url=create_release_data["url"],
            method=create_release_data["method"],
            data=create_release_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("波次列表查询接口")
    @pytest.mark.order(20)
    @pytest.mark.parametrize("wave_release_list_page_info", wave_release_list_page_info)  # 波次列表查询接口
    def test_wave_release_list_page_info(self, wave_release_list_page_info, get_token):
        result = Request().send(
            url=wave_release_list_page_info["url"],
            method=wave_release_list_page_info["method"],
            data=wave_release_list_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("波次列表查看接口")
    @pytest.mark.order(21)
    @pytest.mark.parametrize("wave_release_list_detail_info", wave_release_list_detail_info)  # 波次列表查看接口
    def test_wave_release_list_detail_info(self, wave_release_list_detail_info, get_token):
        result = Request().send(
            url=wave_release_list_detail_info["url"] + str(read_yaml(Path.out_order_middle_path, "wave_id", "data")),
            method=wave_release_list_detail_info["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("拣货单列表查询接口")
    @pytest.mark.order(22)
    @pytest.mark.parametrize("pick_order_page_info", pick_order_page_info)  # 拣货单列表查询接口
    def test_pick_order_page_info(self, pick_order_page_info, get_token):
        result = Request().send(
            url=pick_order_page_info["url"],
            method=pick_order_page_info["method"],
            data=pick_order_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None
        write_yaml(Path.out_order_middle_path, "pick_id", "data", result["body"]['obj'][0]['key'], dict_key=None)

    @allure.title("拣货单详情查看接口")
    @pytest.mark.order(23)
    @pytest.mark.parametrize("pick_order_detail_info", pick_order_detail_info)  # 拣货单详情查看接口
    def test_pick_order_detail_info(self, pick_order_detail_info, get_token):
        result = Request().send(
            url=pick_order_detail_info["url"] + str(read_yaml(Path.out_order_middle_path, "pick_id", "data")),
            method=pick_order_detail_info["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("拣货单打印接口")
    @pytest.mark.order(24)
    @pytest.mark.parametrize("pick_order_print_info", pick_order_print_info)  # 拣货单打印接口
    def test_pick_order_print_info(self, pick_order_print_info, get_token):
        pick_print_id = read_yaml(Path.out_order_middle_path, "pick_id", "data")
        pick_data = pick_order_print_info['data']
        pick_data["pickOrderIdList"] = [f"{pick_print_id}"]
        result = Request().send(
            url=pick_order_print_info["url"],
            method=pick_order_print_info["method"],
            data=pick_order_print_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0]['printData'] is not None

    @allure.title("整件拣货任务指派接口")
    @pytest.mark.order(25)
    @pytest.mark.parametrize("zi_pick_order_assignment", zi_pick_order_assignment)  # 整件拣货任务指派接口
    def test_zi_pick_order_assignment(self, zi_pick_order_assignment, get_token):
        zi_pick_order_assignment['data']['pickOrderId'] = f'{read_yaml(Path.out_order_middle_path, "pick_id", "data")}'
        result = Request().send(
            url=zi_pick_order_assignment["url"],
            method=zi_pick_order_assignment["method"],
            data=zi_pick_order_assignment['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("零货拣货任务指派接口")
    @pytest.mark.order(26)
    @pytest.mark.parametrize("lh_pick_order_assignment", lh_pick_order_assignment)  # 零货拣货任务指派接口
    def test_lh_pick_order_assignment(self, lh_pick_order_assignment, get_token):
        lh_pick_order_assignment['data']['pickOrderId'] = f'{read_yaml(Path.out_order_middle_path, "pick_id", "data")}'
        result = Request().send(
            url=lh_pick_order_assignment["url"],
            method=lh_pick_order_assignment["method"],
            data=lh_pick_order_assignment['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("拣货任务列表查询接口")
    @pytest.mark.order(27)
    @pytest.mark.parametrize("pick_mission_page_info", pick_mission_page_info)  # 拣货任务列表查询接口
    def test_pick_mission_page_info(self, pick_mission_page_info, get_token):
        result = Request().send(
            url=pick_mission_page_info["url"],
            method=pick_mission_page_info["method"],
            data=pick_mission_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None
        write_yaml(Path.out_order_middle_path, "lh_pick_mission_id", "data", result["body"]['obj'][0]['key'],
                   dict_key=None)
        write_yaml(Path.out_order_middle_path, "lh_pick_no", "data", result["body"]['obj'][0]['pickTaskNo'],
                   dict_key=None)
        write_yaml(Path.out_order_middle_path, "zj_pick_mission_id", "data", result["body"]['obj'][1]['key'],
                   dict_key=None)
        write_yaml(Path.out_order_middle_path, "zj_pick_no", "data", result["body"]['obj'][1]['pickTaskNo'],
                   dict_key=None)

    @allure.title("拣货任务查看接口")
    @pytest.mark.order(28)
    @pytest.mark.parametrize("pick_mission_detail_info", pick_mission_detail_info)  # 拣货任务查看接口
    def test_pick_mission_detail_info(self, pick_mission_detail_info, get_token):
        result = Request().send(
            url=pick_mission_detail_info["url"] + str(
                read_yaml(Path.out_order_middle_path, "lh_pick_mission_id", "data")),
            method=pick_mission_detail_info["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("拣货任务分拣单打印接口")
    @pytest.mark.order(29)
    @pytest.mark.parametrize("pick_mission_fjd_print", pick_mission_fjd_print)  # 拣货任务分拣单打印接口
    def test_pick_mission_fjd_print(self, pick_mission_fjd_print, get_token):
        pick_mission_fjd_print['data']['idList'] = [
            f'{read_yaml(Path.out_order_middle_path, "lh_pick_mission_id", "data")}']
        result = Request().send(
            url=pick_mission_fjd_print["url"],
            method=pick_mission_fjd_print["method"],
            data=pick_mission_fjd_print['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0]['printData'] is not None

    @allure.title("拣货任务分拣明细打印接口")
    @pytest.mark.order(30)
    @pytest.mark.parametrize("pick_mission_detail_print", pick_mission_detail_print)  # 拣货任务分拣单打印接口
    def test_pick_mission_detail_print(self, pick_mission_detail_print, get_token):
        pick_mission_detail_print['data']['idList'] = [
            f'{read_yaml(Path.out_order_middle_path, "lh_pick_mission_id", "data")}']
        result = Request().send(
            url=pick_mission_detail_print["url"],
            method=pick_mission_detail_print["method"],
            data=pick_mission_detail_print['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0]['printData'] is not None

    @allure.title("拣货任务纸质拣货单打印接口")
    @pytest.mark.order(31)
    @pytest.mark.parametrize("pick_mission_paper_print", pick_mission_paper_print)  # 拣货任务纸质拣货单打印接口
    def test_pick_mission_paper_print(self, pick_mission_paper_print, get_token):
        pick_mission_data = pick_mission_paper_print['data']
        pick_mission_data['pickTaskId'] = [
            f'{read_yaml(Path.out_order_middle_path, "lh_pick_mission_id", "data")}']
        result = Request().send(
            url=pick_mission_paper_print["url"],
            method=pick_mission_paper_print["method"],
            data=pick_mission_data,
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj']['pickLabelList'] is not None

    @allure.title("PC拣货列表查询接口")
    @pytest.mark.order(32)
    @pytest.mark.parametrize("one_pick_page_info", one_pick_page_info)  # PC拣货列表查询接口
    def test_one_pick_page_info(self, one_pick_page_info, get_token):
        result = Request().send(
            url=one_pick_page_info["url"],
            method=one_pick_page_info["method"],
            data=one_pick_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("PC拣货详情明细查询接口")
    @pytest.mark.order(33)
    @pytest.mark.parametrize("one_pick_detail_info", one_pick_detail_info)  # PC拣货详情明细查询接口
    def test_one_pick_detail_info(self, one_pick_detail_info, get_token):
        result = Request().send(
            url=one_pick_detail_info["url"] + str(read_yaml(Path.out_order_middle_path, "lh_pick_mission_id", "data")),
            method=one_pick_detail_info["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("PC零货一件拣货接口")
    @pytest.mark.order(33)
    @pytest.mark.parametrize("lh_one_pick_data", lh_one_pick_data)  # PC拣货详情明细查询接口
    def test_lh_one_pick_data(self, lh_one_pick_data, get_token):
        result = Request().send(
            url=lh_one_pick_data["url"],
            method=lh_one_pick_data["method"],
            data=[f'{read_yaml(Path.out_order_middle_path, "lh_pick_mission_id", "data")}'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("PC整件一件拣货接口")
    @pytest.mark.order(34)
    @pytest.mark.parametrize("zj_one_pick_data", zj_one_pick_data)  # PC整件一件拣货接口
    def test_zj_one_pick_data(self, zj_one_pick_data, get_token):
        result = Request().send(
            url=zj_one_pick_data["url"],
            method=zj_one_pick_data["method"],
            data=[f'{read_yaml(Path.out_order_middle_path, "zj_pick_mission_id", "data")}'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("整件播种列表查询接口")
    @pytest.mark.order(35)
    @pytest.mark.parametrize("zj_seeding_page_info", zj_seeding_page_info)  # 整件播种列表查询接口
    def test_zj_seeding_page_info(self, zj_seeding_page_info, get_token):
        zj_seeding_page_info['data']['pickTaskNo'] = read_yaml(Path.out_order_middle_path, "zj_pick_no", "data")
        result = Request().send(
            url=zj_seeding_page_info["url"],
            method=zj_seeding_page_info["method"],
            data=zj_seeding_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0]['pickTaskNo'] == read_yaml(
            Path.out_order_middle_path, "zj_pick_no", "data")

    @allure.title("整件播种详情明细查询接口")
    @pytest.mark.order(36)
    @pytest.mark.parametrize("zj_seeding_detail_info", zj_seeding_detail_info)  # 整件播种详情明细查询接口
    def test_zj_seeding_detail_info(self, zj_seeding_detail_info, get_token):
        result = Request().send(
            url=zj_seeding_detail_info["url"] + str(
                read_yaml(Path.out_order_middle_path, "zj_pick_mission_id", "data")),
            method=zj_seeding_detail_info["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("整件播种详情明细查询接口")
    @pytest.mark.order(37)
    @pytest.mark.parametrize("zj_seeding_print_info", zj_seeding_print_info)  # 整件播种详情明细查询接口
    def test_zj_seeding_print_info(self, zj_seeding_print_info, get_token):
        zj_seeding_print_info['data']['idList'] = [
            f'{read_yaml(Path.out_order_middle_path, "zj_pick_mission_id", "data")}']
        result = Request().send(
            url=zj_seeding_print_info["url"],
            method=zj_seeding_print_info["method"],
            data=zj_seeding_print_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0]['printData'] is not None

    @allure.title("整件播种一键分拣接口")
    @pytest.mark.order(38)
    @pytest.mark.parametrize("zj_seeding_data", zj_seeding_data)  # 整件播种一键分拣接口
    def test_zj_seeding_data(self, zj_seeding_data, get_token):
        result = Request().send(
            url=zj_seeding_data["url"] + str(
                read_yaml(Path.out_order_middle_path, "zj_pick_mission_id", "data")),
            method=zj_seeding_data["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("lh播种索取播种任务接口")
    @pytest.mark.order(39)
    @pytest.mark.parametrize("lh_get_seeding_data", lh_get_seeding_data)  # lh播种索取播种任务接口
    def test_lh_get_seeding_data(self, lh_get_seeding_data, get_token):
        result = Request().send(
            url=lh_get_seeding_data["url"] + read_yaml(Path.out_order_middle_path, "lh_pick_no", "data"),
            method=lh_get_seeding_data["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj']['pickTaskNo'] == read_yaml(
            Path.out_order_middle_path, "lh_pick_no", "data")

    @allure.title("lh播种索取播种产品接口")
    @pytest.mark.order(40)
    @pytest.mark.parametrize("lh_get_seeding_product_data", lh_get_seeding_product_data)  # lh播种索取播种产品接口
    def test_lh_get_seeding_product_data(self, lh_get_seeding_product_data, get_token):
        result = Request().send(
            url=lh_get_seeding_product_data[
                    "url"] + f'{read_yaml(Path.out_order_middle_path, "lh_pick_mission_id", "data")}/M12321321',
            method=lh_get_seeding_product_data["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj']['pickTaskNo'] == read_yaml(
            Path.out_order_middle_path, "lh_pick_no", "data")
        write_yaml(Path.out_order_middle_path, "so_info_id", "data", result["body"]['obj']['sowInfoTobId'],
                   dict_key=None)

    @allure.title("零货播种接口")
    @pytest.mark.order(41)
    @pytest.mark.parametrize("lh_seeding_data", lh_seeding_data)  # 零货播种接口
    def test_lh_seeding_data(self, lh_seeding_data, get_token):
        lh_seeding_data['data']['pickTaskNo'] = read_yaml(Path.out_order_middle_path, "lh_pick_no", "data")
        lh_seeding_data['data']['sowInfoTobId'] = read_yaml(Path.out_order_middle_path, "so_info_id", "data")
        result = Request().send(
            url=lh_seeding_data["url"],
            method=lh_seeding_data["method"],
            data=lh_seeding_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("零货分拣单打印接口")
    @pytest.mark.order(42)
    @pytest.mark.parametrize("lh_seeding_fjd_data", lh_seeding_fjd_data)  # 零货分拣单打印接口
    def test_lh_seeding_fjd_data(self, lh_seeding_fjd_data, get_token):
        lh_seeding_fjd_data['data']['idList'] = [
            f'{read_yaml(Path.out_order_middle_path, "lh_pick_mission_id", "data")}']
        result = Request().send(
            url=lh_seeding_fjd_data["url"],
            method=lh_seeding_fjd_data["method"],
            data=lh_seeding_fjd_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0]['printData'] is not None

    @allure.title("零货播种箱标签打印接口")
    @pytest.mark.order(43)
    @pytest.mark.parametrize("lh_seeding_box_label_data", lh_seeding_box_label_data)  # 零货播种箱标签打印接口
    def test_lh_seeding_box_label_data(self, lh_seeding_box_label_data, get_token):
        lh_seeding_box_label_data['data']['idList'] = [
            f'{read_yaml(Path.out_order_middle_path, "lh_pick_mission_id", "data")}']
        result = Request().send(
            url=lh_seeding_box_label_data["url"],
            method=lh_seeding_box_label_data["method"],
            data=lh_seeding_box_label_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0]['pickTaskNo'] is not None
        write_yaml(Path.out_order_middle_path, "lh_pick_box_label", "data", result["body"]['obj'][0]['boxNo'],
                   dict_key=None)

    @allure.title("零货播种拣货容器查看接口")
    @pytest.mark.order(44)
    @pytest.mark.parametrize("lh_get_seeding_pick_data", lh_get_seeding_pick_data)  # 零货播种拣货容器查看接口
    def test_lh_get_seeding_pick_data(self, lh_get_seeding_pick_data, get_token):
        result = Request().send(
            url=lh_get_seeding_pick_data["url"] + str(
                read_yaml(Path.out_order_middle_path, "lh_pick_mission_id", "data")),
            method=lh_get_seeding_pick_data["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("播种分拣信息查看接口")
    @pytest.mark.order(45)
    @pytest.mark.parametrize("lh_get_seeding_fj_data", lh_get_seeding_fj_data)  # 播种分拣信息查看接口
    def test_lh_get_seeding_fj_data(self, lh_get_seeding_fj_data, get_token):
        result = Request().send(
            url=lh_get_seeding_fj_data["url"] + str(
                read_yaml(Path.out_order_middle_path, "lh_pick_mission_id", "data")),
            method=lh_get_seeding_fj_data["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("拆零复核索取箱标签接口")
    @pytest.mark.order(46)
    @pytest.mark.parametrize("cl_fh_get_mission", cl_fh_get_mission)  # 拆零复核索取箱标签接口
    def test_cl_fh_get_mission(self, cl_fh_get_mission, get_token):
        cl_fh_get_mission['data']['boxNo'] = read_yaml(Path.out_order_middle_path, "lh_pick_box_label", "data")
        result = Request().send(
            url=cl_fh_get_mission["url"],
            method=cl_fh_get_mission["method"],
            data=cl_fh_get_mission['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'
        write_yaml(Path.out_order_middle_path, "lh_review_id", "data", result["body"]['obj']['key'], dict_key=None)

    @allure.title("拆零复核箱标签打印接口")
    @pytest.mark.order(47)
    @pytest.mark.parametrize("cl_fh_print_box_no", cl_fh_print_box_no)  # 拆零复核箱标签打印接口
    def test_cl_fh_print_box_no(self, cl_fh_print_box_no, get_token):
        cl_fh_print_box_no['data']['id'] = read_yaml(Path.out_order_middle_path, "lh_review_id", "data")
        result = Request().send(
            url=cl_fh_print_box_no["url"],
            method=cl_fh_print_box_no["method"],
            data=cl_fh_print_box_no['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("拆零复核索取商品接口")
    @pytest.mark.order(48)
    @pytest.mark.parametrize("cl_fh_get_product", cl_fh_get_product)  # 拆零复核索取商品接口
    def test_cl_fh_get_product(self, cl_fh_get_product, get_token):
        result = Request().send(
            url=cl_fh_get_product["url"],
            method=cl_fh_get_product["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("拆零复核完成复核接口")
    @pytest.mark.order(49)
    @pytest.mark.parametrize("cl_fh_down_data", cl_fh_down_data)  # 拆零复核完成复核接口
    def test_cl_fh_down_data(self, cl_fh_down_data, get_token):
        cl_fh_down_data['data']['id'] = str(read_yaml(Path.out_order_middle_path, "lh_review_id", "data"))
        result = Request().send(
            url=cl_fh_down_data["url"],
            method=cl_fh_down_data["method"],
            data=cl_fh_down_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("拆零复核接口")
    @pytest.mark.order(50)
    @pytest.mark.parametrize("cl_fh_save_data", cl_fh_save_data)  # 拆零复核接口
    def test_cl_fh_save_data(self, cl_fh_save_data, get_token):
        cl_fh_save_data['data']['id'] = str(read_yaml(Path.out_order_middle_path, "lh_review_id", "data"))
        result = Request().send(
            url=cl_fh_save_data["url"],
            method=cl_fh_save_data["method"],
            data=cl_fh_save_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("集货复核未索取任务列表查询接口")
    @pytest.mark.order(51)
    @pytest.mark.parametrize("jh_fh_wait_page_info", jh_fh_wait_page_info)  # 集货复核未索取任务列表查询接口
    def test_jh_fh_wait_page_info(self, jh_fh_wait_page_info, get_token):
        result = Request().send(
            url=jh_fh_wait_page_info["url"],
            method=jh_fh_wait_page_info["method"],
            data=jh_fh_wait_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'
        write_yaml(Path.out_order_middle_path, "jh_review_id", "data", result["body"]['obj'][0]['key'], dict_key=None)

    @allure.title("集货复核未索取任务详情接口")
    @pytest.mark.order(52)
    @pytest.mark.parametrize("jh_fh_wait_detail_info", jh_fh_wait_detail_info)  # 集货复核未索取任务详情接口
    def test_jh_fh_wait_detail_info(self, jh_fh_wait_detail_info, get_token):
        jh_review_id = read_yaml(Path.out_order_middle_path, "jh_review_id", "data")
        result = Request().send(
            url=jh_fh_wait_detail_info["url"] + str(jh_review_id),
            method=jh_fh_wait_detail_info["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("集货复核手动集货接口")
    @pytest.mark.order(53)
    @pytest.mark.parametrize("jh_fh_wait_down", jh_fh_wait_down)  # 集货复核手动集货接口
    def test_jh_fh_wait_down(self, jh_fh_wait_down, get_token):
        jh_review_id = read_yaml(Path.out_order_middle_path, "jh_review_id", "data")
        result = Request().send(
            url=jh_fh_wait_down["url"],
            method=jh_fh_wait_down["method"],
            data=[f'{jh_review_id}'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("集货复核列表查询接口")
    @pytest.mark.order(54)
    @pytest.mark.parametrize("jh_fh_page_info", jh_fh_page_info)  # 集货复核列表查询接口
    def test_jh_fh_page_info(self, jh_fh_page_info, get_token):
        result = Request().send(
            url=jh_fh_page_info["url"],
            method=jh_fh_page_info["method"],
            data=jh_fh_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("集货复核索取任务接口")
    @pytest.mark.order(55)
    @pytest.mark.parametrize("jh_fh_task", jh_fh_task)  # 集货复核索取任务接口
    def test_jh_fh_task(self, jh_fh_task, get_token):
        result = Request().send(
            url=jh_fh_task["url"],
            method=jh_fh_task["method"],
            data={},
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("集货复核一键复核接口")
    @pytest.mark.order(56)
    @pytest.mark.parametrize("jh_fh_down", jh_fh_down)  # 集货复核一键复核接口
    def test_jh_fh_down(self, jh_fh_down, get_token):
        jh_review_id = read_yaml(Path.out_order_middle_path, "jh_review_id", "data")
        result = Request().send(
            url=jh_fh_down["url"],
            method=jh_fh_down["method"],
            data={"id": f"{jh_review_id}"},
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("erp新增特殊订单接口")
    @pytest.mark.order(57)
    @pytest.mark.parametrize("create_erp_special_data", create_erp_special_data)  # erp新增特殊订单接口
    def test_create_erp_special_data(self, create_erp_special_data, get_token):
        create_erp_special_data['data']['origNo'] = f"auto-erp-test{generate_random_number()}"
        result = Request().send(
            url=create_erp_special_data["url"],
            method=create_erp_special_data["method"],
            data=create_erp_special_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("调价订单列表查询接口")
    @pytest.mark.order(58)
    @pytest.mark.parametrize("special_order_page_info", special_order_page_info)  # 调价订单列表查询接口
    def test_special_order_page_info(self, special_order_page_info, get_token):
        result = Request().send(
            url=special_order_page_info["url"],
            method=special_order_page_info["method"],
            data=special_order_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200

    @allure.title("调价订单详情明细查询接口")
    @pytest.mark.order(59)
    @pytest.mark.parametrize("special_order_detail_info", special_order_detail_info)  # 调价订单详情明细查询接口
    def test_special_order_detail_info(self, special_order_detail_info, get_token):
        result = Request().send(
            url=special_order_detail_info["url"] + "1982399061266944",
            method=special_order_detail_info["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("调价订单一键出库接口")
    @pytest.mark.order(60)
    @pytest.mark.parametrize("special_out_order_data", special_out_order_data)  # 调价订单一键出库接口
    def test_special_out_order_data(self, special_out_order_data, get_token):
        result = Request().send(
            url=special_out_order_data["url"],
            method=special_out_order_data["method"],
            data=special_out_order_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("出库单打印列表查询接口")
    @pytest.mark.order(61)
    @pytest.mark.parametrize("out_oder_print_page_info", out_oder_print_page_info)  # 出库单打印列表查询接口
    def test_out_oder_print_page_info(self, out_oder_print_page_info, get_token):
        result = Request().send(
            url=out_oder_print_page_info["url"],
            method=out_oder_print_page_info["method"],
            data=out_oder_print_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("出库单打印列表详情查询接口")
    @pytest.mark.order(62)
    @pytest.mark.parametrize("out_oder_print_detail_info", out_oder_print_detail_info)  # 出库单打印列表查询接口
    def test_out_oder_print_detail_info(self, out_oder_print_detail_info, get_token):
        print_id = read_yaml(Path.out_order_middle_path, "so_id", "data")
        result = Request().send(
            url=out_oder_print_detail_info["url"] + str(print_id),
            method=out_oder_print_detail_info["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("冷链交接单打印")
    @pytest.mark.order(63)
    @pytest.mark.parametrize("out_oder_print_cold", out_oder_print_cold)  # 冷链交接单打印
    def test_out_oder_print_cold(self, out_oder_print_cold, get_token):
        out_oder_print_cold['data']['soIdList'] = [read_yaml(Path.out_order_middle_path, "so_id", "data")]
        result = Request().send(
            url=out_oder_print_cold["url"],
            method=out_oder_print_cold["method"],
            data=out_oder_print_cold['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '未查询到要打印的冷链信息'

    @allure.title("出库箱标签打印接口")
    @pytest.mark.order(64)
    @pytest.mark.parametrize("out_oder_print_box_no", out_oder_print_box_no)  # 出库箱标签打印接口
    def test_out_oder_print_box_no(self, out_oder_print_box_no, get_token):
        out_oder_print_box_no['data']['soIdList'] = [read_yaml(Path.out_order_middle_path, "so_id", "data")]
        result = Request().send(
            url=out_oder_print_box_no["url"],
            method=out_oder_print_box_no["method"],
            data=out_oder_print_box_no['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("销售单打印")
    @pytest.mark.order(65)
    @pytest.mark.parametrize("out_oder_print_sale", out_oder_print_sale)  # 销售单打印
    def test_out_oder_print_sale(self, out_oder_print_sale, get_token):
        out_oder_print_sale['data']['soIdList'] = [read_yaml(Path.out_order_middle_path, "so_id", "data")]
        result = Request().send(
            url=out_oder_print_sale["url"],
            method=out_oder_print_sale["method"],
            data=out_oder_print_sale['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("toc出库订单新增")
    @pytest.mark.order(66)
    @pytest.mark.parametrize("create_toc_out_order", create_toc_out_order)  # toc出库订单新增
    def test_create_toc_out_order(self, create_toc_out_order, get_token):
        create_toc_out_order['data']['origNo'] = f"auto-test{generate_random_number()}"
        result = Request().send(
            url=create_toc_out_order["url"],
            method=create_toc_out_order["method"],
            data=create_toc_out_order['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'
        write_yaml(Path.out_order_middle_path, "toc_order_no", "data",
                   create_toc_out_order['data']['origNo'],
                   None)

    @allure.title("toc出库订单生成")
    @pytest.mark.order(67)
    @pytest.mark.parametrize("make_out_order_data", make_out_order_data)  # toc出库订单生成
    def test_toc_make_out_order_data(self, make_out_order_data, get_token):
        detail_id = CommonDatabase().select_data("id", "order_tt_out_order",
                                                 f"orig_no = '{read_yaml(Path.out_order_middle_path, 'toc_order_no', 'data')}'")[
            'id']
        result = Request().send(url=make_out_order_data["url"], method=make_out_order_data["method"],
                                data=[f"{detail_id}"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("tocso分配列表查询接口")
    @pytest.mark.order(68)
    @pytest.mark.parametrize("so_allocation_page_info", so_allocation_page_info)  # tocso分配列表查询接口
    def test_so_toc_allocation_page_info(self, so_allocation_page_info, get_token):
        result = Request().send(url=so_allocation_page_info["url"], method=so_allocation_page_info["method"],
                                data=so_allocation_page_info["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None
        write_yaml(Path.out_order_middle_path, "toc_so_id", "data",
                   result['body']['obj'][0]['id'],
                   None)
        write_yaml(Path.out_order_middle_path, "toc_so_no", "data",
                   result['body']['obj'][0]['soNo'],
                   None)

    @allure.title("tocso手动分配接口")
    @pytest.mark.order(69)
    @pytest.mark.parametrize("so_allocation_data", so_allocation_data)  # so手动分配接口
    def test_so_toc_allocation_data(self, so_allocation_data, get_token):
        result = Request().send(url=so_allocation_data["url"], method=so_allocation_data["method"],
                                data=[f'{read_yaml(Path.out_order_middle_path, "toc_so_id", "data")}'],
                                headers=get_token)
        logger.info(so_allocation_data['title'], result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("toc生成波次接口")
    @pytest.mark.order(70)
    @pytest.mark.parametrize("create_wave_data", create_wave_data)  # 生成波次接口
    def test_toc_create_wave_data(self, create_wave_data, get_token):
        create_wave_data['data']['soIdList'] = [f'{read_yaml(Path.out_order_middle_path, "toc_so_id", "data")}']
        result = Request().send(
            url=create_wave_data["url"],
            method=create_wave_data["method"],
            data=create_wave_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("toc波次下发列表查询接口")
    @pytest.mark.order(71)
    @pytest.mark.parametrize("wave_release_page_info", wave_release_page_info)  # 波次下发列表查询接口
    def test_toc_wave_release_page_info(self, wave_release_page_info, get_token):
        result = Request().send(
            url=wave_release_page_info["url"],
            method=wave_release_page_info["method"],
            data=wave_release_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None
        write_yaml(Path.out_order_middle_path, "toc_wave_id", "data", result["body"]['obj'][0]['key'], dict_key=None)

    @allure.title("toc波次详情明细查询接口")
    @pytest.mark.order(72)
    @pytest.mark.parametrize("wave_release_detail_info", wave_release_detail_info)  # 波次详情明细查询接口
    def test_toc_wave_release_detail_info(self, wave_release_detail_info, get_token):
        result = Request().send(
            url=wave_release_detail_info["url"] + str(read_yaml(Path.out_order_middle_path, "toc_wave_id", "data")),
            method=wave_release_detail_info["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'
        write_yaml(Path.out_order_middle_path, "toc_wave_dt_id", "data", result["body"]['obj'][0]['key'], dict_key=None)

    @allure.title("toc波次暂存区设置接口")
    @pytest.mark.order(73)
    @pytest.mark.parametrize("wave_staging_update", wave_staging_update)  # 波次暂存区设置接口
    def test_toc_wave_staging_update(self, wave_staging_update, get_token):
        result = Request().send(
            url=wave_staging_update["url"],
            method=wave_staging_update["method"],
            data=[f'{read_yaml(Path.out_order_middle_path, "toc_wave_dt_id", "data")}'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("toc波次发布接口")
    @pytest.mark.order(74)
    @pytest.mark.parametrize("create_release_data", create_release_data)  # 波次发布接口
    def test_toc_create_release_data(self, create_release_data, get_token):
        create_release_data['data']['idList'] = [f'{read_yaml(Path.out_order_middle_path, "toc_wave_id", "data")}']
        result = Request().send(
            url=create_release_data["url"],
            method=create_release_data["method"],
            data=create_release_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("toc拣货单列表查询接口")
    @pytest.mark.order(75)
    @pytest.mark.parametrize("pick_order_page_info", pick_order_page_info)  # 拣货单列表查询接口
    def test_toc_pick_order_page_info(self, pick_order_page_info, get_token):
        result = Request().send(
            url=pick_order_page_info["url"],
            method=pick_order_page_info["method"],
            data=pick_order_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None
        write_yaml(Path.out_order_middle_path, "toc_pick_id", "data", result["body"]['obj'][0]['key'], dict_key=None)

    @allure.title("toc整件拣货任务指派接口")
    @pytest.mark.order(76)
    @pytest.mark.parametrize("zi_pick_order_assignment", zi_pick_order_assignment)  # 整件拣货任务指派接口
    def test_toc_zi_pick_order_assignment(self, zi_pick_order_assignment, get_token):
        zi_pick_order_assignment['data'][
            'pickOrderId'] = f'{read_yaml(Path.out_order_middle_path, "toc_pick_id", "data")}'
        result = Request().send(
            url=zi_pick_order_assignment["url"],
            method=zi_pick_order_assignment["method"],
            data=zi_pick_order_assignment['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("toc零货拣货任务指派接口")
    @pytest.mark.order(77)
    @pytest.mark.parametrize("lh_pick_order_assignment", lh_pick_order_assignment)  # 零货拣货任务指派接口
    def test_toc_lh_pick_order_assignment(self, lh_pick_order_assignment, get_token):
        lh_pick_order_assignment['data'][
            'pickOrderId'] = f'{read_yaml(Path.out_order_middle_path, "toc_pick_id", "data")}'
        result = Request().send(
            url=lh_pick_order_assignment["url"],
            method=lh_pick_order_assignment["method"],
            data=lh_pick_order_assignment['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("toc拣货任务列表查询接口")
    @pytest.mark.order(78)
    @pytest.mark.parametrize("pick_mission_page_info", pick_mission_page_info)  # 拣货任务列表查询接口
    def test_toc_pick_mission_page_info(self, pick_mission_page_info, get_token):
        result = Request().send(
            url=pick_mission_page_info["url"],
            method=pick_mission_page_info["method"],
            data=pick_mission_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None
        write_yaml(Path.out_order_middle_path, "toc_lh_pick_mission_id", "data", result["body"]['obj'][0]['key'],
                   dict_key=None)
        write_yaml(Path.out_order_middle_path, "toc_lh_pick_no", "data", result["body"]['obj'][0]['pickOrderNo'],
                   dict_key=None)
        write_yaml(Path.out_order_middle_path, "toc_zj_pick_mission_id", "data", result["body"]['obj'][1]['key'],
                   dict_key=None)
        write_yaml(Path.out_order_middle_path, "toc_zj_pick_no", "data", result["body"]['obj'][1]['pickOrderNo'],
                   dict_key=None)

    @allure.title("tocPC零货一件拣货接口")
    @pytest.mark.order(79)
    @pytest.mark.parametrize("lh_one_pick_data", lh_one_pick_data)  # PC拣货详情明细查询接口
    def test_toc_lh_one_pick_data(self, lh_one_pick_data, get_token):
        result = Request().send(
            url=lh_one_pick_data["url"],
            method=lh_one_pick_data["method"],
            data=[f'{read_yaml(Path.out_order_middle_path, "toc_lh_pick_mission_id", "data")}'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("tocPC整件一件拣货接口")
    @pytest.mark.order(80)
    @pytest.mark.parametrize("zj_one_pick_data", zj_one_pick_data)  # PC整件一件拣货接口
    def test_toc_zj_one_pick_data(self, zj_one_pick_data, get_token):
        result = Request().send(
            url=zj_one_pick_data["url"],
            method=zj_one_pick_data["method"],
            data=[f'{read_yaml(Path.out_order_middle_path, "toc_zj_pick_mission_id", "data")}'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("toc播种获取拣货单任务接口")
    @pytest.mark.order(81)
    @pytest.mark.parametrize("toc_seeding_get_mission", toc_seeding_get_mission)  # toc播种获取拣货单任务接口
    def test_toc_seeding_get_mission(self, toc_seeding_get_mission, get_token):
        result = Request().send(
            url=toc_seeding_get_mission["url"] + read_yaml(Path.out_order_middle_path, "toc_lh_pick_no", "data"),
            method=toc_seeding_get_mission["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("toc播种获取产品信息接口")
    @pytest.mark.order(82)
    @pytest.mark.parametrize("toc_seeding_get_product", toc_seeding_get_product)  # toc播种获取产品信息接口
    def test_toc_seeding_get_product(self, toc_seeding_get_product, get_token):
        result = Request().send(
            url=toc_seeding_get_product[
                    "url"] + f'{read_yaml(Path.out_order_middle_path, "toc_lh_pick_no", "data")}/M12321321',
            method=toc_seeding_get_product["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("toc播种接口")
    @pytest.mark.order(82)
    @pytest.mark.parametrize("toc_seeding_data", toc_seeding_data)  # toc播种接口
    def test_toc_seeding_data(self, toc_seeding_data, get_token):
        result = Request().send(
            url=toc_seeding_data[
                    "url"] + f'{read_yaml(Path.out_order_middle_path, "toc_lh_pick_no", "data")}/M12321321/1/110.11',
            method=toc_seeding_data["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("toc获取so单数据接口")
    @pytest.mark.order(83)
    @pytest.mark.parametrize("toc_fh_get_data", toc_fh_get_data)  # toc获取so单数据接口
    def test_toc_fh_get_data(self, toc_fh_get_data, get_token):
        toc_fh_get_data['data']['soNo'] = f'{read_yaml(Path.out_order_middle_path, "toc_so_no", "data")}'
        result = Request().send(
            url=toc_fh_get_data['url'],
            method=toc_fh_get_data["method"],
            data=toc_fh_get_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'
        write_yaml(Path.out_order_middle_path, "toc_review_id", "data", result["body"]['obj']['key'], dict_key=None)

    @allure.title("toc复核商品明细接口")
    @pytest.mark.order(84)
    @pytest.mark.parametrize("toc_fh_product_data", toc_fh_product_data)  # toc复核商品明细接口
    def test_toc_fh_product_data(self, toc_fh_product_data, get_token):
        toc_fh_product_data['data']['id'] = f'{read_yaml(Path.out_order_middle_path, "toc_review_id", "data")}'
        result = Request().send(
            url=toc_fh_product_data['url'],
            method=toc_fh_product_data["method"],
            data=toc_fh_product_data['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("toc复核完成接口")
    @pytest.mark.order(85)
    @pytest.mark.parametrize("toc_fh_down", toc_fh_down)  # toc复核完成接口
    def test_toc_fh_down(self, toc_fh_down, get_token):
        toc_fh_down['data']['id'] = f'{read_yaml(Path.out_order_middle_path, "toc_review_id", "data")}'
        result = Request().send(
            url=toc_fh_down['url'],
            method=toc_fh_down["method"],
            data=toc_fh_down['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("药检报告打印列表查询接口")
    @pytest.mark.order(86)
    @pytest.mark.parametrize("drug_print_page_info", drug_print_page_info)  # 药检报告打印列表查询接口
    def test_drug_print_page_info(self, drug_print_page_info, get_token):
        result = Request().send(
            url=drug_print_page_info['url'],
            method=drug_print_page_info["method"],
            data=drug_print_page_info['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("药检报告打印接口")
    @pytest.mark.order(87)
    @pytest.mark.parametrize("drug_print_report", drug_print_report)  # 药检报告打印接口
    def test_drug_print_report(self, drug_print_report, get_token):
        drug_print_report['data']['soIdList'] = [read_yaml(Path.out_order_middle_path, "so_id", "data")]
        result = Request().send(
            url=drug_print_report['url'],
            method=drug_print_report["method"],
            data=drug_print_report['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("上游随货同行单打印接口")
    @pytest.mark.order(88)
    @pytest.mark.parametrize("with_product_print", with_product_print)  # 上游随货同行单打印接口
    def test_with_product_printt(self, with_product_print, get_token):
        with_product_print['data']['soIdList'] = [read_yaml(Path.out_order_middle_path, "so_id", "data")]
        result = Request().send(
            url=with_product_print['url'],
            method=with_product_print["method"],
            data=with_product_print['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("发票打印接口")
    @pytest.mark.order(89)
    @pytest.mark.parametrize("invoice_print", invoice_print)  # 发票打印接口
    def test_invoice_print(self, invoice_print, get_token):
        invoice_print['data']['soIdList'] = [read_yaml(Path.out_order_middle_path, "so_id", "data")]
        result = Request().send(
            url=invoice_print['url'],
            method=invoice_print["method"],
            data=invoice_print['data'],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("药检报告详情明细查询接口")
    @pytest.mark.order(90)
    @pytest.mark.parametrize("drug_prin_detail_info", drug_prin_detail_info)  # 药检报告详情明细查询接口
    def test_drug_prin_detail_info(self, drug_prin_detail_info, get_token):
        so_id = read_yaml(Path.out_order_middle_path, "so_id", "data")
        result = Request().send(
            url=drug_prin_detail_info['url'] + str(so_id),
            method=drug_prin_detail_info["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'

    @allure.title("药检报告打印确认接口")
    @pytest.mark.order(90)
    @pytest.mark.parametrize("check_drug_print", check_drug_print)  # 药检报告打印确认接口
    def test_check_drug_print(self, check_drug_print, get_token):
        so_id = read_yaml(Path.out_order_middle_path, "so_id", "data")
        result = Request().send(
            url=check_drug_print['url'],
            method=check_drug_print["method"],
            data=[so_id],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == '成功'
