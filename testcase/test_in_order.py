import pytest
from config.path import *
from utils.get_yaml_data import *
from utils.requests_util import Request
from utils.log import logger
from utils.other_utils import *
from utils.mysql_util import CommonDatabase
import requests
import allure

order_id = read_yaml(Path.middle_data_path, 'rk_order_data', "order_id")
asn_id = read_yaml(Path.middle_data_path, 'rk_order_data', "asn_id")
order_no = read_yaml(Path.middle_data_path, 'rk_order_data', "order_no")
asn_no = read_yaml(Path.middle_data_path, 'rk_order_data', "asn_no")
serial_number_data = read_yaml(Path.middle_data_path, 'rk_order_data', "serial_number")


class TestInOrderData:
    order_type = ["CGDD", "ZPCGDD", "TCSQD", "WDTKSQD", "PFXSTHD", "CGDDZP", "TCSQDZP", "DBRKD", "DBTCD", "LYTHD",
                  "YCRKD"]

    in_order_select_data = read_yaml(Path.in_order_path, "in_order_select_data")
    in_order_create_data = read_yaml(Path.in_order_path, "in_order_create_data")
    in_order_dt_data = read_yaml(Path.in_order_path, "in_order_dt_data")
    create_asn_data = read_yaml(Path.in_order_path, "create_asn_data")
    re_save_order_data = read_yaml(Path.in_order_path, "re_save_order_data")
    select_asn_data = read_yaml(Path.in_order_path, "select_asn_data")
    select_asn_detail_data = read_yaml(Path.in_order_path, "select_asn_detail_data")
    create_re_save_order_data = read_yaml(Path.in_order_path, "create_re_save_order_data")
    select_check_page_info = read_yaml(Path.in_order_path, "select_check_page_info")
    select_check_detail_info = read_yaml(Path.in_order_path, "select_check_detail_info")
    select_check_wait_data = read_yaml(Path.in_order_path, "select_check_wait_data")
    create_check_mission = read_yaml(Path.in_order_path, "create_check_mission")
    create_check_order = read_yaml(Path.in_order_path, "create_check_order")
    select_put_shelf_page_info = read_yaml(Path.in_order_path, "select_put_shelf_page_info")
    select_put_shelf_detail_info = read_yaml(Path.in_order_path, "select_put_shelf_detail_info")
    create_put_shelf_mission = read_yaml(Path.in_order_path, "create_put_shelf_mission")
    select_put_shelf_wait_data = read_yaml(Path.in_order_path, "select_put_shelf_wait_data")
    create_one_put_shelf_mission = read_yaml(Path.in_order_path, "create_one_put_shelf_mission")
    create_put_shelf_order = read_yaml(Path.in_order_path, "create_put_shelf_order")
    select_put_shelf_mission_page_info = read_yaml(Path.in_order_path, "select_put_shelf_mission_page_info")
    with_product_upload_page_info = read_yaml(Path.in_order_path, "with_product_upload_page_info")
    upload_with_product = read_yaml(Path.in_order_path, "upload_with_product")
    save_upload_with_product = read_yaml(Path.in_order_path, "save_upload_with_product")
    upload_with_product_detail_info = read_yaml(Path.in_order_path, "upload_with_product_detail_info")
    in_order_print = read_yaml(Path.in_order_path, "in_order_print")
    with_product_print = read_yaml(Path.in_order_path, "with_product_print")
    check_order_print = read_yaml(Path.in_order_path, "check_order_print")
    check_order_detail_print = read_yaml(Path.in_order_path, "check_order_detail_print")
    put_order_print = read_yaml(Path.in_order_path, "put_order_print")
    select_put_number = read_yaml(Path.in_order_path, "select_put_number")
    put_order_detail_print = read_yaml(Path.in_order_path, "put_order_detail_print")
    select_central_control_page_info = read_yaml(Path.in_order_path, "select_central_control_page_info")
    select_central_control_detail_info = read_yaml(Path.in_order_path, "select_central_control_detail_info")
    update_central_control = read_yaml(Path.in_order_path, "update_central_control")

    @allure.title("入库订单列表查询接口")
    @pytest.mark.order(1)
    @pytest.mark.parametrize("in_order_data", in_order_select_data)  # 获取入库订单列表接口
    def test_in_order_data(self, in_order_data, get_token):
        result = Request().send(url=in_order_data["url"], method=in_order_data["method"], data=in_order_data["data"],
                                headers=get_token)
        logger.info(in_order_data['title'], result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("WMS入库订单新增接口")
    @pytest.mark.order(2)
    @pytest.mark.parametrize("order_type", order_type)  # 为每个订单类型创建单独的用例
    @pytest.mark.parametrize("create_in_order_data", in_order_create_data)  # 入库订单新增接口
    def test_create_in_order_data(self, create_in_order_data, order_type, get_token):
        create_in_order_data['data']['origNo'] = "autotest" + str(generate_random_number())
        create_in_order_data["data"]["orderType"] = order_type

        # 处理不同的订单类型
        if order_type in ["WDTKSQD", "TCSQDZP", "TCSQD"]:
            create_in_order_data["data"]["partnerType"] = "STORE"
            create_in_order_data["data"]["storeId"] = "1848003360018944"
            if order_type in ["TCSQDZP"]:  # 处理 TCSQDZP 和 ZPCGDD
                create_in_order_data['data']['dtReqList'][0]['sourceProductionBatch'] = generate_order_number()
                create_in_order_data['data']['dtReqList'][0]['sourceProductionDate'] = "2024-01"
                create_in_order_data['data']['dtReqList'][0]['sourceInvalidDate'] = "2025-12"
        elif order_type == "PFXSTHD":
            create_in_order_data["data"]["partnerType"] = "CUSTOMER"
            create_in_order_data["data"]["customerId"] = "1891739480969728"
        elif "ZP" in order_type:  # 处理包含 "ZP" 的订单类型
            create_in_order_data["data"]["partnerType"] = "SUPPLIER"
            create_in_order_data["data"]["supplierId"] = "1838234556355072"
            create_in_order_data['data']['dtReqList'][0]['sourceProductionBatch'] = generate_order_number()
            create_in_order_data['data']['dtReqList'][0]['sourceProductionDate'] = "2024-01"
            create_in_order_data['data']['dtReqList'][0]['sourceInvalidDate'] = "2025-12"
        else:
            create_in_order_data["data"]["partnerType"] = "SUPPLIER"
            create_in_order_data["data"]["supplierId"] = "1838234556355072"
            create_in_order_data['data']['dtReqList'][0]['sourceProductionBatch'] = generate_order_number()
            create_in_order_data['data']['dtReqList'][0]['sourceProductionDate'] = "2024-01"
            create_in_order_data['data']['dtReqList'][0]['sourceInvalidDate'] = "2025-12"

        result = Request().send(url=create_in_order_data["url"], method=create_in_order_data["method"],
                                data=create_in_order_data["data"],
                                headers=get_token)
        logger.info(result)

        assert result['code'] == 200 and create_in_order_data['data']['origNo'] == CommonDatabase().select_data(
            "orig_no", "order_tt_in_order",
            f"orig_no='{create_in_order_data['data']['origNo']}'")['orig_no']

        write_yaml(Path().middle_data_path, "rk_order_data", "order_no",
                   create_in_order_data['data']['origNo'], f"{order_type}_order_no")
        write_yaml(Path().middle_data_path, "rk_order_data", "order_id",
                   CommonDatabase().select_data("id", "order_tt_in_order",
                                                f"orig_no='{create_in_order_data['data']['origNo']}'")['id'],
                   f"{order_type}_order_id")

    @allure.title("获取入库订单明细接口")
    @pytest.mark.order(3)
    @pytest.mark.parametrize("order_id_data", [order_id[i] for i in order_id])  # 提取订单id
    @pytest.mark.parametrize("in_order_dt_data", in_order_dt_data)  # 提取入库订单dt_list接口
    def test_in_order_dt_data(self, order_id_data, in_order_dt_data, get_token):
        order_dt_id = {"inOrderId": order_id_data}
        result = Request().send(url=in_order_dt_data["url"], method=in_order_dt_data["method"],
                                data=order_dt_id,
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None
        write_yaml(Path().middle_data_path, "rk_order_data", "order_data", value=result['body']['obj'][0],
                   dict_key=CommonDatabase().select_data("order_type", "order_tt_in_order", f"id = '{order_id_data}'")[
                                "order_type"] + "_order_data")

    @allure.title("生成asn接口")
    @pytest.mark.order(4)
    @pytest.mark.parametrize("order_id_data", [order_id[i] for i in order_id])  # 生成asn
    @pytest.mark.parametrize("create_asn", create_asn_data)
    def test_create_asn_data(self, order_id_data, create_asn, get_token):
        asn_new_data = {**create_asn['data']["dtList"][0],
                        **read_yaml(Path().middle_data_path, "rk_order_data", "order_data")[
                            CommonDatabase().select_data("order_type",
                                                         "order_tt_in_order",
                                                         f"id = '{order_id_data}'")[
                                "order_type"] + "_order_data"
                            ]}
        create_asn['data']["dtList"] = [asn_new_data]
        create_asn['data']['id'] = order_id_data
        create_asn['data']['key'] = order_id_data
        create_asn['data']['extend']['key'] = order_id_data
        create_asn['data']['extend']['id'] = order_id_data
        create_asn['data']['extend']['inOrderId'] = order_id_data
        create_asn['data']['inOrderId'] = order_id_data
        create_asn['data']['orderType'] = CommonDatabase().select_data("order_type", "order_tt_in_order",
                                                                       f"id = '{order_id_data}'")["order_type"]
        create_asn['data']['inOrderNo'] = CommonDatabase().select_data("in_order_no", "order_tt_in_order",
                                                                       f"id = '{order_id_data}'")["in_order_no"]
        create_asn['data']['origNo'] = CommonDatabase().select_data("orig_no", "order_tt_in_order",
                                                                    f"id = '{order_id_data}'")["orig_no"]
        result = Request().send(url=create_asn["url"], method=create_asn["method"],
                                data=create_asn['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and CommonDatabase().select_data("order_type", "order_tt_in_order",
                                                                      f"id = '{order_id_data}'") is not None
        write_yaml(Path().middle_data_path, "rk_order_data", "asn_no", result['body']['obj']['asnNo'],
                   dict_key=CommonDatabase().select_data("order_type", "order_tt_in_order", f"id = '{order_id_data}'")[
                                "order_type"] + "_asn_no")

    @allure.title("提取订单接口")
    @pytest.mark.order(5)
    @pytest.mark.parametrize("re_save_data", create_re_save_order_data)  # 提取订单接口
    def test_re_save_data_data(self, re_save_data, get_token):
        asn_no = read_yaml(Path.middle_data_path, 'rk_order_data', "asn_no")
        for asn_type in asn_no:
            result = Request().send(url=re_save_data["url"] + asn_no[asn_type], method=re_save_data["method"],
                                    data={},
                                    headers=get_token)
            logger.info(result)
            assert result['code'] == 200 and result["body"]['obj'] is not None
            for i in order_id:
                if CommonDatabase().select_data("order_type", "order_tt_in_order", f"id = '{order_id[i]}'")[
                    "order_type"] == result['body']['obj']['asnType']:
                    write_yaml(Path().middle_data_path, "rk_order_data", "asn_id", value=result['body']['obj']['asnId'],
                               dict_key=
                               CommonDatabase().select_data("order_type", "order_tt_in_order", f"id = '{order_id[i]}'")[
                                   "order_type"] + "_asn_id")
                    write_yaml(Path().middle_data_path, "rk_order_data", "asn_data", value=result['body']['obj'],
                               dict_key=
                               CommonDatabase().select_data("order_type", "order_tt_in_order", f"id = '{order_id[i]}'")[
                                   "order_type"] + "_asn_data")
                else:
                    pass

    @allure.title("asn列表查询接口")
    @pytest.mark.order(6)
    @pytest.mark.parametrize("select_asn", select_asn_data)  # asn列表查询接口
    def test_select_asn_data(self, select_asn, get_token):
        result = Request().send(url=select_asn["url"], method=select_asn["method"], data=select_asn["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("asn详情查看接口")
    @pytest.mark.order(7)
    @pytest.mark.parametrize("asn_id_data", [asn_id[i] for i in asn_id])  # asn查看详情接口
    @pytest.mark.parametrize("asn_detail", select_asn_detail_data)
    def test_asn_detail_data(self, asn_id_data, asn_detail, get_token):
        result = Request().send(url=asn_detail["url"] + str(asn_id_data), method=asn_detail["method"], data={},
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("PC收货接口")
    @pytest.mark.order(8)
    @pytest.mark.parametrize("create_re_save_data", re_save_order_data)  # 收货接口
    def test_create_re_save_order(self, create_re_save_data, get_token):
        asn_order = read_yaml(Path().middle_data_path, "rk_order_data", "asn_data")
        for asn_type in asn_order:
            asn_order_data = asn_order[asn_type]
            asn_order_data['waitRecList'][0].update({"isChecked": True,
                                                     "isCheckedNo": True,
                                                     "isSecondCheck": "allFinish",
                                                     "_X_ROW_KEY": "row_1068"})
            create_re_save_data['data']['waitRecList'] = asn_order_data['waitRecList']
            create_re_save_data['data']['dtList'][0]['commonSku'] = asn_order_data['waitRecList'][0]['commonSku']
            # 合并 asn1 和 asn2
            merged_asn = asn_order_data.copy()  # 先复制 asn2 的内容
            merged_asn['waitRecList'] = create_re_save_data['data']['waitRecList']  # 使用 asn1 的 waitRecList
            merged_asn['dtList'] = create_re_save_data['data']['dtList']  # 使用 asn1 的 dtList
            merged_asn['arriveType'] = "TYGSSH"
            merged_asn['shipTool'] = "XSHC"
            merged_asn['shipTime'] = "2024-10-08 00:00"
            merged_asn['arriveTime'] = "2024-10-08 00:00"
            # 提取非 commonSku 的值
            for item in asn_order_data["waitRecList"]:
                # 打印非 commonSku 的值
                for key, value in item.items():
                    if key != "commonSku":
                        merged_asn['dtList'][0][key] = value
            result = Request().send(url=create_re_save_data["url"], method=create_re_save_data["method"],
                                    data=merged_asn,
                                    headers=get_token)
            logger.info(result)
            assert result['code'] == 200 and result['body']['obj']['msg'] == "整单收货完成"

    @allure.title("验收列表查询接口")
    @pytest.mark.order(9)
    @pytest.mark.parametrize("check_page_info", select_check_page_info)  # 验收列表查看详情接口
    @pytest.mark.parametrize("order_no_data", [order_no[i] for i in order_no])
    def test_check_page_info(self, check_page_info, get_token, order_no_data):
        check_page_info['data']['erpOrderNo'] = order_no_data
        check_page_info['data']['createTimeFm'] = create_date_time()['today_str']
        check_page_info['data']['createTimeTo'] = create_date_time()['tomorrow_str']
        result = Request().send(url=check_page_info["url"], method=check_page_info["method"],
                                data=check_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None
        for i in order_id:
            if CommonDatabase().select_data("order_type", "order_tt_in_order", f"id = '{order_id[i]}'")[
                "order_type"] == result['body']['obj'][0]['asnType']:
                write_yaml(Path().middle_data_path, "rk_order_data", "check_id", result['body']['obj'][0]['key'],
                           dict_key=
                           CommonDatabase().select_data("order_type", "order_tt_in_order", f"id = '{order_id[i]}'")[
                               "order_type"] + "_check_id")

    @allure.title("验收详情查看接口")
    @pytest.mark.order(10)
    @pytest.mark.parametrize("check_detail_info", select_check_detail_info)  # 验收详情查询接口
    def test_check_detail_info(self, check_detail_info, get_token):
        for order_type in read_yaml(Path().middle_data_path, "rk_order_data", "check_id"):
            check_id = read_yaml(Path().middle_data_path, "rk_order_data", "check_id")[order_type]
            result = Request().send(url=check_detail_info["url"] + check_id, method=check_detail_info["method"],
                                    headers=get_token)
            logger.info(result)
            assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("索取验收详情查询接口")
    @pytest.mark.order(11)
    @pytest.mark.parametrize("check_wait_data", select_check_wait_data)  # 索取验收详情查询接口
    def test_check_wait_data(self, check_wait_data, get_token):
        for order_type in read_yaml(Path().middle_data_path, "rk_order_data", "check_id"):
            check_id = read_yaml(Path().middle_data_path, "rk_order_data", "check_id")[order_type]
            result = Request().send(url=check_wait_data["url"], method=check_wait_data["method"],
                                    data={"qcId": check_id},
                                    headers=get_token)
            logger.info(result)
            assert result['code'] == 200 and result["body"]['obj'] is not None
            for i in order_id:
                if CommonDatabase().select_data("c.id", "order_tt_in_order a,ib_tt_asn b, ib_tt_qc c",
                                                f"a.id = b.in_order_id and b.id = c.asn_id and a.id ='{order_id[i]}'")[
                    'id'] is not None:
                    if CommonDatabase().select_data("c.id", "order_tt_in_order a,ib_tt_asn b, ib_tt_qc c",
                                                    f"a.id = b.in_order_id and b.id = c.asn_id and a.id ='{order_id[i]}'")[
                        'id'] == \
                            result['body']['obj']['qcId']:
                        write_yaml(Path().middle_data_path, "rk_order_data", "check_data",
                                   result['body']['obj']['waitQcDtList'],
                                   dict_key=
                                   CommonDatabase().select_data("order_type", "order_tt_in_order",
                                                                f"id = '{order_id[i]}'")[
                                       "order_type"] + "_check_data")
                    else:
                        pass
                else:
                    pass

    @allure.title("生成验收任务接口")
    @pytest.mark.order(12)
    @pytest.mark.parametrize("check_mission", create_check_mission)  # 生成验收任务接口
    def test_check_mission(self, check_mission, get_token):
        for order_type in read_yaml(Path().middle_data_path, "rk_order_data", "check_id"):
            check_id = read_yaml(Path().middle_data_path, "rk_order_data", "check_id")[order_type]
            result = Request().send(url=check_mission["url"], method=check_mission["method"],
                                    data={"qcId": check_id},
                                    headers=get_token)
            logger.info(result)
            assert result['code'] == 200 and result["body"]['msg'] == "成功"

    @allure.title("验收接口")
    @pytest.mark.order(13)
    @pytest.mark.parametrize("check_order", create_check_order)  # 验收接口
    def test_check_order(self, check_order, get_token):
        check_data = read_yaml(Path().middle_data_path, "rk_order_data", "check_data")
        for data_type in check_data:
            create_check_data = check_data[data_type]
            create_check_data[0].update({"checkedFlagApproval": True,
                                         "checkedFlag": True,
                                         "_X_ROW_KEY": "row_601",
                                         "checkResultDesc": None,
                                         "handleMeasure": None})
            create_check_data[0].update({"checkResult": "HG"})
            data = {"dtList": [create_check_data[0]], "qcId": create_check_data[0]["qcId"], "mac": "B0-7B-25-29-F7-04"}
            result = Request().send(url=check_order["url"], method=check_order["method"], data=data,
                                    headers=get_token)
            logger.info(result)
            assert result['code'] == 200 and result["body"]['obj']['msg'] == "整单验收完成"

    @allure.title("上架列表查询接口")
    @pytest.mark.order(14)
    @pytest.mark.parametrize("put_shelf_page_info", select_put_shelf_page_info)  # 上架列表查询接口
    @pytest.mark.parametrize("order_no_data", [order_no[i] for i in order_no])
    def test_put_shelf_page_info(self, put_shelf_page_info, get_token, order_no_data):
        put_shelf_page_info['data']['erpOrderNo'] = order_no_data
        put_shelf_page_info['data']['createTimeFm'] = create_date_time()['today_str']
        put_shelf_page_info['data']['createTimeTo'] = create_date_time()['tomorrow_str']
        result = Request().send(url=put_shelf_page_info["url"], method=put_shelf_page_info["method"],
                                data=put_shelf_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None
        for i in order_id:
            if CommonDatabase().select_data("order_type", "order_tt_in_order", f"id = '{order_id[i]}'")[
                "order_type"] == result['body']['obj'][0]['asnType']:
                write_yaml(Path().middle_data_path, "rk_order_data", "put_shelf_id", result['body']['obj'][0]['key'],
                           dict_key=
                           CommonDatabase().select_data("order_type", "order_tt_in_order", f"id = '{order_id[i]}'")[
                               "order_type"] + "_put_shelf_id")

    @allure.title("上架详情查询接口")
    @pytest.mark.order(15)
    @pytest.mark.parametrize("put_shelf_detail_info", select_put_shelf_detail_info)  # 上架详情查询接口
    def test_put_shelf_detail_info(self, put_shelf_detail_info, get_token):
        for order_type in read_yaml(Path().middle_data_path, "rk_order_data", "put_shelf_id"):
            put_shelf_id = read_yaml(Path().middle_data_path, "rk_order_data", "put_shelf_id")[order_type]
            result = Request().send(url=put_shelf_detail_info["url"] + put_shelf_id,
                                    method=put_shelf_detail_info["method"],
                                    headers=get_token)
            logger.info(result)
            assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("非直配订单生成上架任务接口")
    @pytest.mark.order(16)
    @pytest.mark.parametrize("put_shelf_mission", create_put_shelf_mission)  # 非直配订单生成上架任务接口
    def test_put_shelf_mission(self, put_shelf_mission, get_token):
        for order_type in read_yaml(Path().middle_data_path, "rk_order_data", "put_shelf_id"):
            if "CGDDZP_put_shelf_id" not in order_type and "TCSQDZP_put_shelf_id" not in order_type:
                put_shelf_id = read_yaml(Path().middle_data_path, "rk_order_data", "put_shelf_id")[order_type]
                result = Request().send(url=put_shelf_mission["url"], method=put_shelf_mission["method"],
                                        data={"putShelfId": put_shelf_id},
                                        headers=get_token)
                logger.info(result)
                assert result['code'] == 200 and result["body"]['msg'] == "成功"

    @allure.title("入库批量操作-直配订单一件上架接口")
    @pytest.mark.order(17)
    @pytest.mark.parametrize("one_put_shelf", create_one_put_shelf_mission)  # 直配订单一件上架接口
    def test_one_put_shelf(self, one_put_shelf, get_token):
        for order_type in read_yaml(Path().middle_data_path, "rk_order_data", "put_shelf_id"):
            if "CGDDZP_put_shelf_id" in order_type or "TCSQDZP_put_shelf_id" in order_type:
                put_shelf_id = CommonDatabase().select_data("d.id",
                                                            f"ib_tt_qc a, ib_tt_put_shelf b,ib_tt_asn c, order_tt_in_order d where a.id = b.origin_order_id and a.asn_id = c.id and c.in_order_id = d.id and b.id = {read_yaml(Path().middle_data_path, 'rk_order_data', 'put_shelf_id')[order_type]}")[
                    'id']
                result = Request().send(url=one_put_shelf["url"], method=one_put_shelf["method"],
                                        data=[f"{put_shelf_id}"],
                                        headers=get_token)
                logger.info(result)
                assert result['code'] == 200 and result["body"]['msg'] == "成功"

    @allure.title("索取上架详情接口")
    @pytest.mark.order(18)
    @pytest.mark.parametrize("put_shelf_wait_data", select_put_shelf_wait_data)  # 索取上架详情接口
    def test_put_shelf_wait_data(self, put_shelf_wait_data, get_token):
        for order_type in read_yaml(Path().middle_data_path, "rk_order_data", "put_shelf_id"):
            if "CGDDZP_put_shelf_id" not in order_type and "TCSQDZP_put_shelf_id" not in order_type:
                put_shelf_id = read_yaml(Path().middle_data_path, "rk_order_data", "put_shelf_id")[order_type]
                result = Request().send(url=put_shelf_wait_data["url"], method=put_shelf_wait_data["method"],
                                        data={"putShelfId": put_shelf_id},
                                        headers=get_token)
                logger.info(result)
                assert result['code'] == 200 and result["body"]['obj'] is not None
                for i in order_id:
                    if \
                            CommonDatabase().select_data("b.id",
                                                         "ib_tt_qc a, ib_tt_put_shelf b,ib_tt_asn c, order_tt_in_order d",
                                                         f" a.id = b.origin_order_id and a.asn_id = c.id and c.in_order_id = d.id and d.id ='{order_id[i]}'")[
                                'id'] is not None:
                        if CommonDatabase().select_data("b.id",
                                                        "ib_tt_qc a, ib_tt_put_shelf b,ib_tt_asn c, order_tt_in_order d",
                                                        f" a.id = b.origin_order_id and a.asn_id = c.id and c.in_order_id = d.id and d.id ='{order_id[i]}'")[
                            'id'] == \
                                result['body']['obj']['waitPutShelfTaskDtList'][0]['putShelfId']:
                            write_yaml(Path().middle_data_path, "rk_order_data", "put_shelf_data",
                                       result['body']['obj']['waitPutShelfTaskDtList'],
                                       dict_key=
                                       CommonDatabase().select_data("order_type", "order_tt_in_order",
                                                                    f"id = '{order_id[i]}'")[
                                           "order_type"] + "_put_shelf_data")
                        else:
                            pass
                    else:
                        pass

    @allure.title("上架接口")
    @pytest.mark.order(19)
    @pytest.mark.parametrize("put_shelf_order", create_put_shelf_order)  # 上架接口
    def test_put_order(self, put_shelf_order, get_token):
        put_shelf_data = read_yaml(Path().middle_data_path, "rk_order_data", "put_shelf_data")
        for data_type in put_shelf_data:
            create_put_data = put_shelf_data[data_type]
            create_put_data[0].update({"sourceContainerNo": None,
                                       "checkedFlag": None,
                                       "_X_ROW_KEY": "row_539"})
            data = {"dtList": [create_put_data[0]]}
            print(data)
            result = Request().send(url=put_shelf_order["url"], method=put_shelf_order["method"], data=data,
                                    headers=get_token)
            logger.info(result)
            assert result['code'] == 200

    @allure.title("上架任务列表查询接口")
    @pytest.mark.order(20)
    @pytest.mark.parametrize("put_shelf_mission_page_info", select_put_shelf_mission_page_info)  # 上架任务列表查询接口
    def test_put_shelf_mission_page_info(self, put_shelf_mission_page_info, get_token):
        result = Request().send(url=put_shelf_mission_page_info["url"], method=put_shelf_mission_page_info["method"],
                                data=put_shelf_mission_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("随货同行单列表查询接口")
    @pytest.mark.order(21)
    @pytest.mark.parametrize("with_product_upload_page_info", with_product_upload_page_info)  # 随货同行单列表查询接口
    def test_with_product_upload_page_info(self, with_product_upload_page_info, get_token):
        result = Request().send(url=with_product_upload_page_info["url"],
                                method=with_product_upload_page_info["method"],
                                data=with_product_upload_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None

    @allure.title("随货同行单上传附件接口")
    @pytest.mark.order(22)
    @pytest.mark.parametrize("upload_with_product", upload_with_product)  # 随货同行单上传附件
    @pytest.mark.parametrize("asn_no_data", [asn_no[i] for i in asn_no])
    def test_upload_with_product(self, upload_with_product, get_token, asn_no_data):
        result = requests.post(
            url=upload_with_product["url"],
            files={
                "file": ('tp1.png', open(Path.picture_path, 'rb'), 'image/png')
            },
            data={
                'moduleName': f'ib/{asn_no_data}'
            },
            headers={"Authorization": get_token["Authorization"]}
        ).json()
        logger.info(result)
        assert result['code'] == 200 and result['obj'] is not None
        for i in order_id:
            if CommonDatabase().select_data("order_type", "order_tt_in_order", f"id = '{order_id[i]}'")[
                "order_type"] == CommonDatabase().select_data("asn_type", "ib_tt_asn", f"asn_no = '{asn_no_data}'")[
                "asn_type"]:
                write_yaml(Path().middle_data_path, "rk_order_data", "upload_data", result['obj'],
                           dict_key=
                           CommonDatabase().select_data("asn_type", "ib_tt_asn", f"asn_no = '{asn_no_data}'")[
                               "asn_type"] + "_upload_data")

    @allure.title("随货同行单保存接口")
    @pytest.mark.order(23)
    @pytest.mark.parametrize("save_upload_with_product", save_upload_with_product)  # 随货同行单保存接口
    @pytest.mark.parametrize("asn_id_data", [asn_id[i] for i in asn_id])
    def test_save_upload_with_product(self, save_upload_with_product, get_token, asn_id_data):
        file_url = read_yaml(Path().middle_data_path, "rk_order_data", "upload_data")
        save_upload_with_product['data']['dtList'][0]['fileUrl'] = file_url[CommonDatabase().select_data(
            "asn_type", "ib_tt_asn", f"id = '{asn_id_data}'")["asn_type"] + "_upload_data"
                                                                            ]
        save_upload_with_product['data']['asnId'] = asn_id_data
        result = Request().send(url=save_upload_with_product["url"],
                                method=save_upload_with_product["method"],
                                data=save_upload_with_product['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == "成功"

    @allure.title("冷链文件保存接口")
    @pytest.mark.order(24)
    @pytest.mark.parametrize("save_cold_upload_with_product", save_upload_with_product)  # 冷链文件上传保存接口
    @pytest.mark.parametrize("asn_id_data", [asn_id[i] for i in asn_id])
    def test_save_cold_upload_with_product(self, save_cold_upload_with_product, get_token, asn_id_data):
        file_url = read_yaml(Path().middle_data_path, "rk_order_data", "upload_data")
        save_cold_upload_with_product['data']['dtList'][0]['fileUrl'] = file_url[CommonDatabase().select_data(
            "asn_type", "ib_tt_asn", f"id = '{asn_id_data}'")["asn_type"] + "_upload_data"
                                                                                 ]
        save_cold_upload_with_product['data']['asnId'] = asn_id_data
        save_cold_upload_with_product['data']['fileType'] = "LLWJ"
        result = Request().send(url=save_cold_upload_with_product["url"],
                                method=save_cold_upload_with_product["method"],
                                data=save_cold_upload_with_product['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == "成功"

    @allure.title("随货同行单查看接口")
    @pytest.mark.order(25)
    @pytest.mark.parametrize("upload_with_product_detail_info", upload_with_product_detail_info)  # 随后同行单查看接口
    @pytest.mark.parametrize("asn_id_data", [asn_id[i] for i in asn_id])
    def test_upload_with_product_detail_info(self, upload_with_product_detail_info, get_token, asn_id_data):
        result = Request().send(url=upload_with_product_detail_info["url"] + str(asn_id_data),
                                method=upload_with_product_detail_info["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None

    @allure.title("入库单打印列表接口")
    @pytest.mark.order(26)
    @pytest.mark.parametrize("order_print", in_order_print)  # 入库单打印列表接口
    def test_in_order_print(self, order_print, get_token):
        result = Request().send(url=order_print["url"],
                                method=order_print["method"],
                                data=order_print['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['total'] > 0

    @allure.title("随货同行单打印接口")
    @pytest.mark.order(27)
    @pytest.mark.parametrize("with_product_print", with_product_print)  # 随货同行单打印接口
    @pytest.mark.parametrize("asn_id_data", [asn_id[i] for i in asn_id])
    def test_with_product_print(self, with_product_print, get_token, asn_id_data):
        with_product_print['data']['asnIdList'] = [f"{asn_id_data}"]
        result = Request().send(url=with_product_print["url"],
                                method=with_product_print["method"],
                                data=with_product_print['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0]['asnNo'] == CommonDatabase().select_data(
            "asn_no", "ib_tt_asn", f"id = '{asn_id_data}'")["asn_no"]

    @allure.title("验收单打印接口")
    @pytest.mark.order(28)
    @pytest.mark.parametrize("check_order_print", check_order_print)  # 验收单打印接口
    @pytest.mark.parametrize("asn_id_data", [asn_id[i] for i in asn_id])
    def test_check_order_print(self, check_order_print, get_token, asn_id_data):
        check_id = \
            CommonDatabase().select_data("a.id", "ib_tt_qc a, ib_tt_asn b",
                                         f"a.asn_id = b.id and b.id = '{asn_id_data}'")[
                'id']
        check_order_print['data']['qcIdList'] = [f"{check_id}"]
        result = Request().send(url=check_order_print["url"],
                                method=check_order_print["method"],
                                data=check_order_print['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0]['printTemplateTypeName'] == "验收单打印模版"

    @allure.title("验收标签打印接口")
    @pytest.mark.order(29)
    @pytest.mark.parametrize("check_order_detail_print", check_order_detail_print)  # 验收标签打印接口
    @pytest.mark.parametrize("asn_id_data", [asn_id[i] for i in asn_id])
    def test_check_order_detail_print(self, check_order_detail_print, get_token, asn_id_data):
        check_data_id = \
            CommonDatabase().select_data("c.id", "ib_tt_qc a, ib_tt_asn b, ib_tt_qc_dt c",
                                         f"a.asn_id = b.id and a.id=c.qc_id and b.id = '{asn_id_data}'")[
                'id']
        check_order_detail_print['data']['qcDtIdList'] = [f"{check_data_id}"]
        result = Request().send(url=check_order_detail_print["url"],
                                method=check_order_detail_print["method"],
                                data=check_order_detail_print['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0]['asnNo'] == CommonDatabase().select_data(
            "asn_no", "ib_tt_asn", f"id = '{asn_id_data}'")["asn_no"]

    @allure.title("上架单打印接口")
    @pytest.mark.order(30)
    @pytest.mark.parametrize("put_order_print", put_order_print)  # 上架单打印
    @pytest.mark.parametrize("asn_id_data", [asn_id[i] for i in asn_id])
    def test_put_order_print(self, put_order_print, get_token, asn_id_data):
        put_shelf_id = CommonDatabase().select_data("b.id",
                                                    "ib_tt_qc a, ib_tt_put_shelf b,ib_tt_asn c, order_tt_in_order d",
                                                    f"a.id = b.origin_order_id and a.asn_id = c.id and c.in_order_id = d.id and c.id = '{asn_id_data}';")[
            'id']
        put_order_print['data']['putShelfIdList'] = [f"{put_shelf_id}"]
        result = Request().send(url=put_order_print["url"],
                                method=put_order_print["method"],
                                data=put_order_print['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == "成功"

    @allure.title("上架标签列表查询接口")
    @pytest.mark.order(31)
    @pytest.mark.parametrize("select_put_number", select_put_number)  # 上架标签列表查询接口
    @pytest.mark.parametrize("asn_id_data", [asn_id[i] for i in asn_id])
    def test_select_put_number(self, select_put_number, get_token, asn_id_data):
        put_shelf_id = CommonDatabase().select_data("b.id",
                                                    "ib_tt_qc a, ib_tt_put_shelf b,ib_tt_asn c, order_tt_in_order d",
                                                    f"a.id = b.origin_order_id and a.asn_id = c.id and c.in_order_id = d.id and c.id = '{asn_id_data}';")[
            'id']
        select_put_number['data']['putShelfId'] = f"{put_shelf_id}"
        result = Request().send(url=select_put_number["url"],
                                method=select_put_number["method"],
                                data=select_put_number['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'] is not None
        for i in order_id:

            if CommonDatabase().select_data("order_type", "order_tt_in_order", f"id = '{order_id[i]}'")[
                "order_type"] == CommonDatabase().select_data("asn_type", "ib_tt_asn", f"id = '{asn_id_data}'")[
                "asn_type"]:
                write_yaml(Path().middle_data_path, "rk_order_data", "serial_number",
                           result['body']['obj'][0]['serialNumber'],
                           dict_key=
                           CommonDatabase().select_data("asn_type", "ib_tt_asn", f"id = '{asn_id_data}'")[
                               "asn_type"] + "_serial_number")

    @allure.title("上架标签打印接口")
    @pytest.mark.order(32)
    @pytest.mark.parametrize("put_order_detail_print", put_order_detail_print)  # 上架标签打印接口
    @pytest.mark.parametrize("serial_number_data", [serial_number_data[i] for i in serial_number_data])
    def test_put_order_detail_print(self, put_order_detail_print, get_token, serial_number_data):
        put_order_detail_print['data']['serialNumberList'] = [serial_number_data]
        result = Request().send(url=put_order_detail_print["url"],
                                method=put_order_detail_print["method"],
                                data=put_order_detail_print['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == "成功"

    @allure.title("入库中控台列表查询接口")
    @pytest.mark.order(33)
    @pytest.mark.parametrize("central_control_page_info", select_central_control_page_info)  # 入库中控台列表查询接口
    def test_central_control_page_info(self, central_control_page_info, get_token):
        result = Request().send(url=central_control_page_info["url"],
                                data=central_control_page_info['data'],
                                headers=get_token,
                                method=central_control_page_info["method"])
        logger.info(result)
        assert result['code'] == 200 and result["body"]['obj'][0] is not None
        write_yaml(Path().middle_data_path, "rk_order_data", "wait_center_control", result['body']['obj'][0]['key'],
                   dict_key="data")

    @allure.title("入库中控台获取订单商品明细接口")
    @pytest.mark.order(34)
    @pytest.mark.parametrize("central_control_detail_info", select_central_control_detail_info)  # 入库中控台获取订单商品明细接口
    def test_central_control_detail_info(self, central_control_detail_info, get_token):
        central_control_detail_info['data']['asnId'] = \
            read_yaml(Path().middle_data_path, "rk_order_data", "wait_center_control")['data']
        result = Request().send(url=central_control_detail_info["url"],
                                method=central_control_detail_info["method"],
                                data=central_control_detail_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['total'] == 1
        write_yaml(Path().middle_data_path, "rk_order_data", "wait_center_control_data",
                   result['body']['obj'][0],
                   dict_key="data")
