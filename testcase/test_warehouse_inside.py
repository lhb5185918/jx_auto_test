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
    warehouse_stock_lock_page_info = read_yaml(Path.warehouse_inside_path, "warehouse_stock_lock_page_info")
    warehouse_stock_lock_detail_info = read_yaml(Path.warehouse_inside_path, "warehouse_stock_lock_detail_info")
    create_warehouse_stock_lock = read_yaml(Path.warehouse_inside_path, "create_warehouse_stock_lock")
    check_stock_status = read_yaml(Path.warehouse_inside_path, "check_stock_status")
    select_un_lock_page_info = read_yaml(Path.warehouse_inside_path, "select_un_lock_page_info")
    select_un_lock_detail_info = read_yaml(Path.warehouse_inside_path, "select_un_lock_detail_info")
    create_warehouse_un_stock_lock = read_yaml(Path.warehouse_inside_path, "create_warehouse_un_stock_lock")
    check_un_stock_status = read_yaml(Path.warehouse_inside_path, "check_un_stock_status")
    warehouse_color_management = read_yaml(Path.warehouse_inside_path, "warehouse_color_management")
    replenish_management_page_info = read_yaml(Path.warehouse_inside_path, "replenish_management_page_info")
    replenish_management_detail_info = read_yaml(Path.warehouse_inside_path, "replenish_management_detail_info")
    create_replenish_management = read_yaml(Path.warehouse_inside_path, "create_replenish_management")
    make_replenish_management = read_yaml(Path.warehouse_inside_path, "make_replenish_management")
    cancel_replenish_management = read_yaml(Path.warehouse_inside_path, "cancel_replenish_management")
    so_replenish_management_detail = read_yaml(Path.warehouse_inside_path, "so_replenish_management_detail")
    replenish_management_detail = read_yaml(Path.warehouse_inside_path, "replenish_management_detail")
    create_move_order = read_yaml(Path.warehouse_inside_path, "create_move_order")
    select_move_order_page_info = read_yaml(Path.warehouse_inside_path, "select_move_order_page_info")
    mave_warehouse_location_page_info = read_yaml(Path.warehouse_inside_path, "mave_warehouse_location_page_info")
    mave_warehouse_location_page_detail = read_yaml(Path.warehouse_inside_path, "mave_warehouse_location_page_detail")
    create_move_warehouse = read_yaml(Path.warehouse_inside_path, "create_move_warehouse")
    make_move_location = read_yaml(Path.warehouse_inside_path, "make_move_location")
    move_location_detail = read_yaml(Path.warehouse_inside_path, "move_location_detail")
    mave_location_page_info = read_yaml(Path.warehouse_inside_path, "mave_location_page_info")
    mave_location_page_detail = read_yaml(Path.warehouse_inside_path, "mave_location_page_detail")
    create_move_location = read_yaml(Path.warehouse_inside_path, "create_move_location")
    make_location = read_yaml(Path.warehouse_inside_path, "make_move_location")
    move_detail = read_yaml(Path.warehouse_inside_path, "move_detail")
    select_inventory_mission_page_info = read_yaml(Path.warehouse_inside_path, "select_inventory_mission_page_info")
    select_inventory_mission_detail_info = read_yaml(Path.warehouse_inside_path, "select_inventory_mission_detail_info")
    select_inventory_page_info = read_yaml(Path.warehouse_inside_path, "select_inventory_mission_page_info")
    select_inventory_detail_info = read_yaml(Path.warehouse_inside_path, "select_inventory_mission_detail_info")
    select_inventory_detail = read_yaml(Path.warehouse_inside_path, "select_inventory_detail")
    create_inventory = read_yaml(Path.warehouse_inside_path, "create_inventory")
    print_inventory = read_yaml(Path.warehouse_inside_path, "print_inventory")
    write_inventory_page = read_yaml(Path.warehouse_inside_path, "write_inventory_page")
    plan_inventory_page = read_yaml(Path.warehouse_inside_path, "plan_inventory_page")
    profit_inventory_page = read_yaml(Path.warehouse_inside_path, "profit_inventory_page")
    profit_inventory_detail_page = read_yaml(Path.warehouse_inside_path, "profit_inventory_detail_page")
    create_profit_inventory = read_yaml(Path.warehouse_inside_path, "create_profit_inventory")
    check_profit_inventory = read_yaml(Path.warehouse_inside_path, "check_profit_inventory")
    check_profit_detail = read_yaml(Path.warehouse_inside_path, "check_profit_detail")
    consume_tree_page_info = read_yaml(Path.warehouse_inside_path, "consume_tree_page_info")
    create_consume = read_yaml(Path.warehouse_inside_path, "create_consume")
    delete_consume = read_yaml(Path.warehouse_inside_path, "delete_consume")
    consume_management_page_info = read_yaml(Path.warehouse_inside_path, "consume_management_page_info")
    create_consume_management = read_yaml(Path.warehouse_inside_path, "create_consume_management")
    down_shelf_page_info = read_yaml(Path.warehouse_inside_path, "down_shelf_page_info")
    down_shelf_detail_info = read_yaml(Path.warehouse_inside_path, "down_shelf_detail_info")
    get_down_shelf_mission = read_yaml(Path.warehouse_inside_path, "get_down_shelf_mission")
    get_down_shelf_mission_detail = read_yaml(Path.warehouse_inside_path, "get_down_shelf_mission_detail")
    down_shelf_mission = read_yaml(Path.warehouse_inside_path, "down_shelf_mission")

    @allure.title("库存锁定列表查询接口")
    @pytest.mark.parametrize("stock_lock_data", warehouse_stock_lock_page_info)  # 库存锁定列表查询接口
    def test_stock_lock_data_page_info(self, stock_lock_data, get_token):
        result = Request().send(url=stock_lock_data["url"], method=stock_lock_data["method"],
                                data=stock_lock_data["data"],
                                headers=get_token)
        logger.info(stock_lock_data['title'], result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("库存锁定明细详情查询接口")
    @pytest.mark.parametrize("stock_lock_detail_data", warehouse_stock_lock_detail_info)  # 库存锁定明细详情查询接口
    def test_stock_lock_data_detail_info(self, stock_lock_detail_data, get_token):
        result = Request().send(url=stock_lock_detail_data["url"], method=stock_lock_detail_data["method"],
                                data=stock_lock_detail_data["data"],
                                headers=get_token)
        logger.info(stock_lock_detail_data['title'], result)
        assert result['code'] == 200 and result["body"] is not None
        write_yaml(Path.inside_middle_data_path, "stock_detail_data", "data", result["body"]['obj'][0], None)

    @allure.title("新增库存锁定接口")
    @pytest.mark.parametrize("ware_house_data", create_warehouse_stock_lock)  # 新增库存锁定接口
    def test_create_stock_lock_data(self, ware_house_data, get_token):
        detail_data = read_yaml(Path.inside_middle_data_path, "stock_detail_data", "data")
        ware_house_data['data']['dtList'][0] = detail_data
        ware_house_data['data']['dtList'][0].update({
            "_X_ROW_KEY": "row_195",
            "frozenNum": "0.001"
        })
        ware_house_data['data']['dtList'][0][
            'key'] = f"{detail_data['skuId']}{detail_data['lotCode']}{detail_data['batchNo']}{detail_data['ownerId']}{detail_data['orgId']}{detail_data['stockStatus']}"
        ware_house_data['data']['dtList'][0]['frozenQty'] = "0.001"
        result = Request().send(url=ware_house_data["url"], method=ware_house_data["method"],
                                data=ware_house_data["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("库存锁定审核接口")
    @pytest.mark.parametrize("check_stock_data", check_stock_status)  # 库存锁定审核接口
    def test_check_stock_data(self, check_stock_data, get_token):
        get_id_data = read_yaml(Path.warehouse_inside_path,
                                "warehouse_stock_lock_page_info")[0]
        stock_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
            'key']
        result = Request().send(url=check_stock_data["url"] + str(stock_id), method=check_stock_data["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("库存解锁列表查询接口")
    @pytest.mark.parametrize("un_stock_lock_data", select_un_lock_page_info)  # 库存解锁列表查询接口
    def test_un_stock_lock_data_page_info(self, un_stock_lock_data, get_token):
        result = Request().send(url=un_stock_lock_data["url"], method=un_stock_lock_data["method"],
                                data=un_stock_lock_data["data"],
                                headers=get_token)
        logger.info(un_stock_lock_data['title'], result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("库存解锁详情查询接口")
    @pytest.mark.parametrize("un_stock_lock_detail_data", select_un_lock_detail_info)  # 库存锁定明细详情查询接口
    def test_un_stock_lock_data_detail_info(self, un_stock_lock_detail_data, get_token):
        result = Request().send(url=un_stock_lock_detail_data["url"], method=un_stock_lock_detail_data["method"],
                                data=un_stock_lock_detail_data["data"],
                                headers=get_token)
        logger.info(un_stock_lock_detail_data['title'], result)
        assert result['code'] == 200 and result["body"] is not None
        write_yaml(Path.inside_middle_data_path, "un_stock_detail_data", "data", result["body"]['obj'][0], None)

    @allure.title("新增库存解锁接口")
    @pytest.mark.parametrize("un_stock_ware_house_data", create_warehouse_un_stock_lock)  # 新增库存解锁接口
    def test_create_un_stock_lock_data(self, un_stock_ware_house_data, get_token):
        detail_data = read_yaml(Path.inside_middle_data_path, "un_stock_detail_data", "data")
        un_stock_ware_house_data['data']['dtList'][0] = detail_data
        un_stock_ware_house_data['data']['dtList'][0].update({
            "_X_ROW_KEY": "row_30",
            "unfrozenNum": "0.001",
            "unfrozenQty": "0.001"
        })
        un_stock_ware_house_data['data']['dtList'][0][
            'key'] = f"{detail_data['skuId']}{detail_data['lotCode']}{detail_data['batchNo']}{detail_data['ownerId']}{detail_data['orgId']}{detail_data['stockStatus']}"
        un_stock_ware_house_data['data']['dtList'][0]['frozenQty'] = 0.001
        result = Request().send(url=un_stock_ware_house_data["url"], method=un_stock_ware_house_data["method"],
                                data=un_stock_ware_house_data["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("库存解锁审核接口")
    @pytest.mark.parametrize("check_un_stock_data", check_un_stock_status)  # 库存锁定审核接口
    def test_check_un_stock_data(self, check_un_stock_data, get_token):
        get_id_data = read_yaml(Path.warehouse_inside_path,
                                "select_un_lock_page_info")[0]
        un_stock_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
            'key']
        result = Request().send(url=check_un_stock_data["url"] + str(un_stock_id), method=check_un_stock_data["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("库存色标查询接口")
    @pytest.mark.parametrize("warehouse_color_management", warehouse_color_management)  # 库存色标查询接口
    def test_warehouse_color_management(self, warehouse_color_management, get_token):
        result = Request().send(url=warehouse_color_management["url"], method=warehouse_color_management["method"],
                                data=warehouse_color_management["data"],
                                headers=get_token)
        logger.info(warehouse_color_management['title'], result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("补货管理列表查询接口")
    @pytest.mark.parametrize("replenish_management_page_info", replenish_management_page_info)  # 补货管理列表查询接口
    def test_replenish_management_page_info(self, replenish_management_page_info, get_token):
        result = Request().send(url=replenish_management_page_info["url"],
                                method=replenish_management_page_info["method"],
                                data=replenish_management_page_info["data"],
                                headers=get_token)
        logger.info(replenish_management_page_info['title'], result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("补货管理明细详情查询接口")
    @pytest.mark.parametrize("replenish_management_detail_info", replenish_management_detail_info)  # 补货管理明细详情查询接口
    def test_replenish_management_detail_info(self, replenish_management_detail_info, get_token):
        result = Request().send(url=replenish_management_detail_info["url"],
                                method=replenish_management_detail_info["method"],
                                data=replenish_management_detail_info["data"],
                                headers=get_token)
        logger.info(replenish_management_detail_info['title'], result)
        assert result['code'] == 200 and result["body"] is not None
        write_yaml(Path.inside_middle_data_path, "replenish_management_detail_data", "data", result["body"]['obj'][0],
                   None)

    @allure.title("新增主动补货订单接口")
    @pytest.mark.parametrize("create_replenish_management", create_replenish_management)  # 新增主动补货订单接口
    def test_create_replenish_management(self, create_replenish_management, get_token):
        detail_data = read_yaml(Path.inside_middle_data_path, "replenish_management_detail_data", "data")
        create_replenish_management['data']['dtList'][0] = detail_data
        create_replenish_management['data']['dtList'][0].update({
            "fmLotId": 1801492418384384,
            "fmLotName": "ZJ01",
            "fmZoneId": 1773131364520448,
            "fmZoneName": "01整件库区",
            "fmPackageAttrName": "整件",
            "fmLotPackageAttr": "ZJ",
            "_X_ROW_KEY": "row_1043",
            "rowNo": 1,
            "planPieceQty": "1",
            "planNum": "1",
            "ZJplanQty": "105.000",
            "planQty": "105.000",
            "toLotId": "1887627269329408",
            "toZoneName": "01零货库区",
            "toLotName": "LH0020",
            "toPackageAttrName": "零货"
        })
        result = Request().send(url=create_replenish_management["url"], method=create_replenish_management["method"],
                                data=create_replenish_management["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("主动补货订单审核下发接口")
    @pytest.mark.parametrize("make_replenish_management", make_replenish_management)  # 主动补货订单审核下发接口
    def test_make_replenish_management(self, make_replenish_management, get_token):
        get_id_data = read_yaml(Path.warehouse_inside_path,
                                "replenish_management_page_info")[0]
        replenish_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
            'key']
        result = Request().send(url=make_replenish_management["url"], method=make_replenish_management["method"],
                                data=[f"{replenish_id}"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("主动补货取消接口")
    @pytest.mark.parametrize("cancel_replenish_management", cancel_replenish_management)  # 主动补货取消接口
    def test_cancel_replenish_management(self, cancel_replenish_management, get_token):
        get_id_data = read_yaml(Path.warehouse_inside_path,
                                "replenish_management_page_info")[0]
        replenish_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
            'key']
        result = Request().send(url=cancel_replenish_management["url"], method=cancel_replenish_management["method"],
                                data=[f"{replenish_id}"],
                                headers=get_token)
        logger.info(result)
        assert result['body']['code'] == 1001

    @allure.title("补货-缺货明细列表查询接口")
    @pytest.mark.parametrize("so_replenish_management_detail", so_replenish_management_detail)  # 补货-缺货明细列表查询接口
    def test_so_replenish_management_detail(self, so_replenish_management_detail, get_token):
        result = Request().send(url=so_replenish_management_detail["url"],
                                method=so_replenish_management_detail["method"],
                                data=so_replenish_management_detail["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("补货单查看接口")
    @pytest.mark.parametrize("replenish_management_detail", replenish_management_detail)  # 补货单查看接口
    def test_replenish_management_detail(self, replenish_management_detail, get_token):
        get_id_data = read_yaml(Path.warehouse_inside_path,
                                "replenish_management_page_info")[0]
        replenish_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
            'key']
        result = Request().send(url=replenish_management_detail["url"] + str(replenish_id),
                                method=replenish_management_detail["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("erp-货转单新增接口")
    @pytest.mark.parametrize("create_move_order", create_move_order)  # "erp-货转单新增接口
    def test_create_move_order(self, create_move_order, get_token):
        create_move_order['data']['origNo'] = f"HZD-{generate_random_number()}"
        result = Request().send(url=create_move_order["url"],
                                method=create_move_order["method"],
                                data=create_move_order["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]['msg'] == "成功"

    @allure.title("erp-货转单列表查询接口")
    @pytest.mark.parametrize("select_move_order_page_info", select_move_order_page_info)  # erp-货转单列表查询接口
    def test_select_move_order_page_info(self, select_move_order_page_info, get_token):
        result = Request().send(url=select_move_order_page_info["url"],
                                method=select_move_order_page_info["method"],
                                data=select_move_order_page_info["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("移库单列表查询接口")
    @pytest.mark.parametrize("mave_warehouse_location_page_info", mave_warehouse_location_page_info)  # 移库单列表查询接口
    def test_mave_warehouse_location_page_info(self, mave_warehouse_location_page_info, get_token):
        result = Request().send(url=mave_warehouse_location_page_info["url"],
                                method=mave_warehouse_location_page_info["method"],
                                data=mave_warehouse_location_page_info["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("移库单可移库商品详情查询接口")
    @pytest.mark.parametrize("mave_warehouse_location_page_detail",
                             mave_warehouse_location_page_detail)  # 移库单可移库商品详情查询接口
    def test_mave_warehouse_location_page_detail(self, mave_warehouse_location_page_detail, get_token):
        result = Request().send(url=mave_warehouse_location_page_detail["url"],
                                method=mave_warehouse_location_page_detail["method"],
                                data=mave_warehouse_location_page_detail["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None
        write_yaml(Path.inside_middle_data_path, "move_warehouse_location_data", "data", result["body"]['obj'][0],
                   None)

    @allure.title("移库单新增接口")
    @pytest.mark.parametrize("create_move_warehouse", create_move_warehouse)  # 移库单新增接口
    def test_create_move_warehouse(self, create_move_warehouse, get_token):
        detail_data = read_yaml(Path.inside_middle_data_path, "move_warehouse_location_data", "data")
        create_move_warehouse["data"]["moveLotOrderDtReqList"][0] = detail_data
        create_move_warehouse["data"]["moveLotOrderDtReqList"][0]['planMoveQty'] = "1"
        create_move_warehouse["data"]["moveLotOrderDtReqList"][0].update({
            "batchNoKey": None,
            "productionBatch": f"{detail_data['invBatchPO']['productionBatch']}",
            "productionDate": f"{detail_data['invBatchPO']['productionDate']}",
            "instoreDate": f"{detail_data['invBatchPO']['instoreDate']}",
            "invalidDate": f"{detail_data['invBatchPO']['invalidDate']}",
            "po": None,
            "asnNo": None,
            "sterileNo": "",
            "sterileInvaliDate": "",
            "originalOutOrderErpNo": None,
            "optimistic": None,
            "invBatchRuleId": None,
            "ownerId": None,
            "sysSkuCode": None,
            "skuName": "氨糖",
            "origSys": None,
            "spec": "50g",
            "ephedrine": None,
            "tradeName": "氨糖",
            "skuCategoryId": None,
            "brandName": "",
            "barcode": "9093281111",
            "mainUnit": "青岛海尔科技有限公司",
            "length": None,
            "width": None,
            "height": None,
            "vol": None,
            "grossWeight": None,
            "netWeight": None,
            "abc": None,
            "zjAbc": None,
            "mfgId": None,
            "mfg": None,
            "outFactoryCode": None,
            "model": None,
            "originCountry": "山东省青岛市市北区",
            "logistics": None,
            "isBatchManage": None,
            "isValidity": None,
            "validityType": None,
            "validityDay": 0,
            "warmValidityDay": None,
            "isValuables": None,
            "isCombination": None,
            "isGift": None,
            "isConsumables": None,
            "isChangeable": None,
            "isProneToMistakes": None,
            "isHeteromorphicProduct": None,
            "perQty": 105,
            "midPackQty": None,
            "isEnable": None,
            "auditOpinion": None,
            "auditStatus": None,
            "auditTime": None,
            "auditName": None,
            "barcodeTwo": None,
            "barcodeThree": None,
            "taxCode": None,
            "taxName": None,
            "taxFee": None,
            "tempControl": "CW",
            "scatteredProperties": None,
            "gmpCertNo": None,
            "approvalNumber": "国药准字氨糖",
            "categoryPrincipal": None,
            "permitHolder": None,
            "qtyStandard": None,
            "mnemonicCode": None,
            "limitSaleDay": None,
            "routeOfAdministration": None,
            "tempMax": None,
            "tempMin": None,
            "minInvoicingUnit": None,
            "packFactoryId": None,
            "productFormType": None,
            "isLimitMidPack": None,
            "hasAnaleptic": None,
            "tempCondition": None,
            "diCode": None,
            "erpUpdaterName": None,
            "erpUpdateTime": None,
            "erpCreatorName": None,
            "erpCreateTime": None,
            "creditType": None,
            "medicalInsuranceCode": None,
            "instrumentModel": None,
            "entrustMfgId": None,
            "skuBarCode": "9093281111",
            "unitName": "青岛海尔科技有限公司",
            "specName": "50g",
            "productionBatchNo": f"{detail_data['invBatchPO']['productionBatch']}",
            "wkTypeName": "常温",
            "_X_ROW_KEY": "row_1194",
            "toLotId": "1887627269329408",
            "toZoneId": 1773127985943040,
            "toZoneName": "01零货库区",
            "toZoneCode": "KQBM01",
            "toLotCode": "LH0020",
            "toLotName": "LH0020",
            "planNum": "1",
            "plantMoveNum": None
        })
        result = Request().send(url=create_move_warehouse["url"], method=create_move_warehouse["method"],
                                data=create_move_warehouse["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("移库单审核下发接口")
    @pytest.mark.parametrize("make_move_location", make_move_location)  # 移库单审核下发接口
    def test_make_move_location(self, make_move_location, get_token):
        get_id_data = read_yaml(Path.warehouse_inside_path,
                                "mave_warehouse_location_page_info")[0]
        location_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
            'key']
        result = Request().send(url=make_move_location["url"] + str(location_id), method=make_move_location["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("移库单详情查看接口")
    @pytest.mark.parametrize("move_location_detail", move_location_detail)  # 移库单详情查看接口
    def test_move_location_detail(self, move_location_detail, get_token):
        get_id_data = read_yaml(Path.warehouse_inside_path,
                                "mave_warehouse_location_page_info")[0]
        location_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
            'key']
        result = Request().send(url=move_location_detail["url"] + str(location_id),
                                method=move_location_detail["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("移位单列表查询接口")
    @pytest.mark.parametrize("mave_location_page_info", mave_location_page_info)  # 移位单列表查询接口
    def test_mave_location_page_info(self, mave_location_page_info, get_token):
        result = Request().send(url=mave_location_page_info["url"],
                                method=mave_location_page_info["method"],
                                data=mave_location_page_info["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("移位单可移位产品详情查询接口")
    @pytest.mark.parametrize("mave_location_page_detail",
                             mave_location_page_detail)  # 移位单可移位产品详情查询接口
    def test_mave_location_page_detail(self, mave_location_page_detail, get_token):
        result = Request().send(url=mave_location_page_detail["url"],
                                method=mave_location_page_detail["method"],
                                data=mave_location_page_detail["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None
        write_yaml(Path.inside_middle_data_path, "mave_location_page_info_data", "data", result["body"]['obj'][0],
                   None)

    @allure.title("移位单新增接口")
    @pytest.mark.parametrize("create_move_location", create_move_location)  # 移位单新增接口
    def test_create_move_location(self, create_move_location, get_token):
        detail_data = read_yaml(Path.inside_middle_data_path, "mave_location_page_info_data", "data")
        create_move_location["data"]["dtList"][0] = detail_data
        create_move_location["data"]["dtList"][0]['zjQty'] = 0
        create_move_location["data"]["dtList"][0].update({
            "fmLotId": 1784448505156096,
            "fmLotName": "LH0009",
            "fmZoneId": 1773127985943040,
            "fmZoneName": "01零货库区",
            "fmPackageAttrName": "零货",
            "_X_ROW_KEY": "row_38",
            "toZoneName": "01零货库区",
            "toLotId": "1887627269329408",
            "toLotName": "LH0020",
            "toPackageAttrName": "零货",
            "rowNo": 1,
            "planPieceQty": "0.001",
            "planNum": None,
            "planQty": "0.001"
        })
        result = Request().send(url=create_move_location["url"], method=create_move_location["method"],
                                data=create_move_location["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("移位审核下发接口")
    @pytest.mark.parametrize("make_location", make_location)  # 移位审核下发接口
    def test_make_location(self, make_location, get_token):
        get_id_data = read_yaml(Path.warehouse_inside_path,
                                "mave_location_page_info")[0]
        location_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
            'key']
        result = Request().send(url=make_location["url"] + str(location_id), method=make_location["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("移位查看详情接口")
    @pytest.mark.parametrize("move_detail", move_detail)  # 移位查看详情接口
    def test_move_detail(self, move_detail, get_token):
        get_id_data = read_yaml(Path.warehouse_inside_path,
                                "mave_location_page_info")[0]
        location_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
            'key']
        result = Request().send(url=move_detail["url"] + str(location_id), method=move_detail["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("盘点任务列表查询接口")
    @pytest.mark.parametrize("select_inventory_mission_page_info", select_inventory_mission_page_info)  # 盘点任务列表查询接口
    def test_select_inventory_mission_page_info(self, select_inventory_mission_page_info, get_token):
        result = Request().send(url=select_inventory_mission_page_info["url"],
                                method=select_inventory_mission_page_info["method"],
                                data=select_inventory_mission_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("盘点任务详情查询接口")
    @pytest.mark.parametrize("select_inventory_mission_detail_info", select_inventory_mission_detail_info)  # 盘点任务详情查询接口
    def test_select_inventory_mission_detail_info(self, select_inventory_mission_detail_info, get_token):
        get_id_data = read_yaml(Path.warehouse_inside_path,
                                "select_inventory_mission_page_info")[0]
        location_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
            'key']
        result = Request().send(url=select_inventory_mission_detail_info["url"] + str(location_id),
                                method=select_inventory_mission_detail_info["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("盘点列表查询接口")
    @pytest.mark.parametrize("select_inventory_page_info", select_inventory_page_info)  # 盘点列表查询接口
    def test_select_inventory_page_info(self, select_inventory_page_info, get_token):
        result = Request().send(url=select_inventory_page_info["url"],
                                method=select_inventory_page_info["method"],
                                data=select_inventory_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("盘点详情查看查询接口")
    @pytest.mark.parametrize("select_inventory_detail_info", select_inventory_detail_info)  # 盘点详情查看查询接口
    def test_select_inventory_detail_info(self, select_inventory_detail_info, get_token):
        get_id_data = read_yaml(Path.warehouse_inside_path,
                                "select_inventory_page_info")[0]
        location_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
            'key']
        result = Request().send(url=select_inventory_detail_info["url"] + str(location_id),
                                method=select_inventory_detail_info["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    # @allure.title("盘点明细详情查询接口")
    # @pytest.mark.parametrize("select_inventory_detail", select_inventory_detail)  # 盘点明细详情查询接口
    # def test_select_inventory_detail(self, select_inventory_detail, get_token):
    #     result = Request().send(url=select_inventory_detail["url"],
    #                             method=select_inventory_detail["method"],
    #                             data=select_inventory_detail["data"],
    #                             headers=get_token)
    #     logger.info(result)
    #     assert result['code'] == 200 and result["body"] is not None
        # write_yaml(Path.inside_middle_data_path, "mave_location_page_info_data", "data", result["body"]['obj'][0],
        #            None)
    #
    # @allure.title("盘点单新增接口")
    # @pytest.mark.parametrize("create_inventory", create_inventory)  # 盘点单新增接口
    # def test_create_inventory(self, create_inventory, get_token):
    #     result = Request().send(url=create_inventory["url"],
    #                             method=create_inventory["method"],
    #                             data=create_inventory["data"],
    #                             headers=get_token)
    #     logger.info(result)
    #     assert result['code'] == 200 and result["body"] is not None
    #
    # @allure.title("盘点单打印接口")
    # @pytest.mark.parametrize("print_inventory", print_inventory)  # 盘点单打印接口
    # def test_print_inventory(self, print_inventory, get_token):
    #     get_id_data = read_yaml(Path.warehouse_inside_path,
    #                             "select_inventory_page_info")[0]
    #     location_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
    #         'key']
    #     print_data = {
    #         "mac": "B0-7B-25-29-F7-04",
    #         "idList": [
    #             f"{location_id}"
    #         ]
    #     }
    #     result = Request().send(url=print_inventory["url"],
    #                             method=print_inventory["method"],
    #                             data=print_data,
    #                             headers=get_token)
    #     logger.info(result)
    #     assert result['code'] == 200 and result["body"] is not None
    #
    # @allure.title("盘点录入接口")
    # @pytest.mark.parametrize("write_inventory_page", write_inventory_page)  # 盘点录入接口
    # def test_write_inventory_page(self, write_inventory_page, get_token):
    #     get_id_data = read_yaml(Path.warehouse_inside_path,
    #                             "select_inventory_page_info")[0]
    #     location_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
    #         'key']
    #     result = Request().send(url=write_inventory_page["url"] + str(location_id),
    #                             method=write_inventory_page["method"],
    #                             headers=get_token)
    #     logger.info(result)
    #     assert result['code'] == 200 and result["body"] is not None
    #
    # @allure.title("盘点计划列表查询接口")
    # @pytest.mark.parametrize("plan_inventory_page", plan_inventory_page)  # 盘点计划列表查询接口
    # def test_plan_inventory_page(self, plan_inventory_page, get_token):
    #     result = Request().send(url=plan_inventory_page["url"],
    #                             method=plan_inventory_page["method"],
    #                             data=plan_inventory_page["data"],
    #                             headers=get_token)
    #     logger.info(result)
    #     assert result['code'] == 200 and result["body"] is not None
    #
    # @allure.title("盘盈盘亏单列表查询接口")
    # @pytest.mark.parametrize("profit_inventory_page", profit_inventory_page)  # 盘盈盘亏单列表查询接口
    # def test_profit_inventory_page(self, profit_inventory_page, get_token):
    #     result = Request().send(url=profit_inventory_page["url"],
    #                             method=profit_inventory_page["method"],
    #                             data=profit_inventory_page["data"],
    #                             headers=get_token)
    #     logger.info(result)
    #     assert result['code'] == 200 and result["body"] is not None
    #
    # @allure.title("盘盈盘亏单详情明细查询接口")
    # @pytest.mark.parametrize("profit_inventory_detail_page", profit_inventory_detail_page)  # 盘盈盘亏单详情明细查询接口
    # def test_profit_inventory_detail_page(self, profit_inventory_detail_page, get_token):
    #     result = Request().send(url=profit_inventory_detail_page["url"],
    #                             method=profit_inventory_detail_page["method"],
    #                             data=profit_inventory_detail_page["data"],
    #                             headers=get_token)
    #     logger.info(result)
    #     assert result['code'] == 200 and result["body"] is not None
    #     write_yaml(Path.inside_middle_data_path, "profit_inventory_detail_page_data", "data", result["body"]['obj'][0],
    #                None)
    #
    # @allure.title("盘盈盘亏单新增接口")
    # @pytest.mark.parametrize("create_profit_inventory", create_profit_inventory)  # 盘盈盘亏单新增接口
    # def test_create_profit_inventory(self, create_profit_inventory, get_token):
    #     detail_data = read_yaml(Path.inside_middle_data_path, "profit_inventory_detail_page_data", "data")
    #     create_profit_inventory["data"]["dtList"][0] = detail_data
    #     create_profit_inventory["data"]["dtList"][0].update({
    #         "_X_ROW_KEY": "row_323",
    #         "adjReason": "YXDS",
    #         "adjPieceQty": "1",
    #         "adjQty": 1,
    #         "afterAdjQty": f"{detail_data['planPdQty'] + 1}"
    #     })
    #     result = Request().send(url=create_profit_inventory["url"], method=create_profit_inventory["method"],
    #                             data=create_profit_inventory["data"],
    #                             headers=get_token)
    #     logger.info(result)
    #     assert result['code'] == 200 and result["body"] is not None
    #
    # @allure.title("盘盈盘亏单审核接口")
    # @pytest.mark.parametrize("check_profit_inventory", check_profit_inventory)  # 盘点录入接口
    # def test_check_profit_inventory(self, check_profit_inventory, get_token):
    #     get_id_data = read_yaml(Path.warehouse_inside_path,
    #                             "profit_inventory_page")[0]
    #     location_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
    #         'key']
    #     result = Request().send(url=check_profit_inventory["url"] + str(location_id),
    #                             method=check_profit_inventory["method"],
    #                             headers=get_token)
    #     logger.info(result)
    #     assert result['code'] == 200 and result["body"] is not None
    #
    # @allure.title("盘盈盘亏单查看详情接口")
    # @pytest.mark.parametrize("check_profit_detail", check_profit_detail)  # 盘盈盘亏单查看详情接口
    # def test_check_profit_detail(self, check_profit_detail, get_token):
    #     get_id_data = read_yaml(Path.warehouse_inside_path,
    #                             "profit_inventory_page")[0]
    #     location_id = requests.post(get_id_data['url'], json=get_id_data["data"], headers=get_token).json()['obj'][0][
    #         'key']
    #     result = Request().send(url=check_profit_detail["url"] + str(location_id),
    #                             method=check_profit_detail["method"],
    #                             headers=get_token)
    #     logger.info(result)
    #     assert result['code'] == 200 and result["body"] is not None

    @allure.title("耗材树查询接口")
    @pytest.mark.parametrize("consume_tree_page_info", consume_tree_page_info)  # 耗材树查询接口
    def test_consume_tree_page_info(self, consume_tree_page_info, get_token):
        result = Request().send(url=consume_tree_page_info["url"],
                                method=consume_tree_page_info["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("耗材创建接口")
    @pytest.mark.parametrize("create_consume", create_consume)  # 耗材创建接口
    def test_create_consume(self, create_consume, get_token):
        result = Request().send(url=create_consume["url"],
                                method=create_consume["method"],
                                data=create_consume["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("耗材删除接口")
    @pytest.mark.parametrize("delete_consume", delete_consume)  # 耗材删除接口
    def test_delete_consume(self, delete_consume, get_token):
        consume_id = CommonDatabase().select_data("id", "inv_tt_consumables", "category_code = 'auto1'")['id']
        result = Request().send(url=delete_consume["url"] + str(consume_id),
                                method=delete_consume["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("耗材管理列表查询接口")
    @pytest.mark.parametrize("consume_management_page_info", consume_management_page_info)  # 耗材管理列表查询接口
    def test_consume_management_page_info(self, consume_management_page_info, get_token):
        result = Request().send(url=consume_management_page_info["url"],
                                method=consume_management_page_info["method"],
                                data=consume_management_page_info["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("耗材管理新增接口")
    @pytest.mark.parametrize("create_consume_management", create_consume_management)  # 耗材管理新增接口
    def test_create_consume_management(self, create_consume_management, get_token):
        result = Request().send(url=create_consume_management["url"],
                                method=create_consume_management["method"],
                                data=create_consume_management["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("下架列表查询接口")
    @pytest.mark.parametrize("down_shelf_page_info", down_shelf_page_info)  # 下架列表查询接口
    def test_down_shelf_page_info(self, down_shelf_page_info, get_token):
        result = Request().send(url=down_shelf_page_info["url"],
                                method=down_shelf_page_info["method"],
                                data=down_shelf_page_info["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None
        write_yaml(Path.inside_middle_data_path, "down_shelf_no", "data", result["body"]["obj"][0]["downTaskNo"], None)

    @allure.title("下架列明细查询接口")
    @pytest.mark.parametrize("down_shelf_detail_info", down_shelf_detail_info)  # 下架列明细查询接口
    def test_down_shelf_detail_info(self, down_shelf_detail_info, get_token):
        result = Request().send(
            url=down_shelf_detail_info["url"] + read_yaml(Path.inside_middle_data_path, "down_shelf_no", "data"),
            method=down_shelf_detail_info["method"],
            headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("下架任务索取接口")
    @pytest.mark.parametrize("get_down_shelf_mission", get_down_shelf_mission)  # 下架任务索取接口
    def test_get_down_shelf_mission(self, get_down_shelf_mission, get_token):
        result = Request().send(url=get_down_shelf_mission["url"],
                                method=get_down_shelf_mission["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("获取下架任务详情接口")
    @pytest.mark.parametrize("get_down_shelf_mission_detail", get_down_shelf_mission_detail)  # 获取下架任务详情接口
    def test_get_down_shelf_mission_detail(self, get_down_shelf_mission_detail, get_token):
        result = Request().send(url=get_down_shelf_mission_detail["url"],
                                method=get_down_shelf_mission_detail["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None
        write_yaml(Path.inside_middle_data_path, "down_shelf_data", "data", result["body"]["obj"][0], None)

    @allure.title("下架接口")
    @pytest.mark.parametrize("down_shelf_mission", down_shelf_mission)  # 下架接口
    def test_down_shelf_mission(self, down_shelf_mission, get_token):
        result = Request().send(url=down_shelf_mission["url"],
                                method=down_shelf_mission["method"],
                                data=[
                                    f"{read_yaml(Path.inside_middle_data_path, 'down_shelf_data', 'data')['downTaskNo']}"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
