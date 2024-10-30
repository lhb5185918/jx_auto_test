import pytest
from config.path import *
from utils.get_yaml_data import *
from utils.requests_util import Request
from utils.log import logger
from utils.other_utils import *
from utils.mysql_util import CommonDatabase
import requests
import allure


class TestGspManagement:
    select_product_change_status_page_info = read_yaml(Path.gsp_management_path,
                                                       "select_product_change_status_page_info")
    select_product_change_status_detail_info = read_yaml(Path.gsp_management_path,
                                                         "select_product_change_status_detail_info")
    create_product_change_status = read_yaml(Path.gsp_management_path, "create_product_change_status")
    audit_product_change_status = read_yaml(Path.gsp_management_path, "audit_product_change_status")
    product_change_status_detail_info = read_yaml(Path.gsp_management_path, "product_change_status_detail_info")
    select_yh_management_page_info = read_yaml(Path.gsp_management_path, "select_yh_management_page_info")
    select_yh_management_detail_info = read_yaml(Path.gsp_management_path, "select_yh_management_detail_info")
    create_yh_management = read_yaml(Path.gsp_management_path, "create_yh_management")
    select_yh_mission_page_info = read_yaml(Path.gsp_management_path, "select_yh_mission_page_info")
    select_yh_mission_detail_info = read_yaml(Path.gsp_management_path, "select_yh_mission_detail_info")
    create_yh_mission = read_yaml(Path.gsp_management_path, "create_yh_mission")
    select_yh_files = read_yaml(Path.gsp_management_path, "select_yh_files")
    select_check_quality_page_info = read_yaml(Path.gsp_management_path, "select_check_quality_page_info")
    select_check_quality_detail_info = read_yaml(Path.gsp_management_path, "select_check_quality_detail_info")
    create_check_quality = read_yaml(Path.gsp_management_path, "create_check_quality")
    select_check_quality_detail = read_yaml(Path.gsp_management_path, "select_check_quality_detail")
    audit_check_quality = read_yaml(Path.gsp_management_path, "audit_check_quality")
    select_audit_quality_list_info = read_yaml(Path.gsp_management_path, "select_audit_quality_list_info")
    select_audit_quality_detail_info = read_yaml(Path.gsp_management_path, "select_audit_quality_detail_info")
    create_audit_quality = read_yaml(Path.gsp_management_path, "create_audit_quality")
    audit_quality_audit = read_yaml(Path.gsp_management_path, "audit_quality_audit")
    select_bhg_product_page_info = read_yaml(Path.gsp_management_path, "select_bhg_product_page_info")
    select_bhg_product_detail_info = read_yaml(Path.gsp_management_path, "select_bhg_product_detail_info")
    create_bhg_product = read_yaml(Path.gsp_management_path, "create_bhg_product")
    bhg_product_audit = read_yaml(Path.gsp_management_path, "select_bhg_product_audit")
    erp_audit_bhg_product = read_yaml(Path.gsp_management_path, "erp_audit_bhg_product")
    bhg_down_shelf = read_yaml(Path.gsp_management_path, "bhg_down_shelf")
    select_destroy_product_page_info = read_yaml(Path.gsp_management_path, "select_destroy_product_page_info")
    select_destroy_product_detail_info = read_yaml(Path.gsp_management_path, "select_destroy_product_detail_info")
    create_destroy_product = read_yaml(Path.gsp_management_path, "create_destroy_product")
    audit_destroy_product = read_yaml(Path.gsp_management_path, "audit_destroy_product")
    second_audit_destroy_product = read_yaml(Path.gsp_management_path, "second_audit_destroy_product")
    select_near_expire_date_page_info = read_yaml(Path.gsp_management_path, "select_near_expire_date_page_info")
    select_unsalable_page_info = read_yaml(Path.gsp_management_path, "select_unsalable_page_info")
    select_unsalable_detail_info = read_yaml(Path.gsp_management_path, "select_unsalable_detail_info")
    create_unsalable_data = read_yaml(Path.gsp_management_path, "create_unsalable_data")
    select_unsalable_list_page_info = read_yaml(Path.gsp_management_path, "select_unsalable_list_page_info")
    select_immediate_list_page_info = read_yaml(Path.gsp_management_path, "select_immediate_list_page_info")

    @allure.title("产品状态变化管理列表查询接口")
    @pytest.mark.parametrize("select_product_change_status_page_info",
                             select_product_change_status_page_info)  # 产品状态变化管理列表查询接口
    def test_select_product_change_status_page_info(self, select_product_change_status_page_info, get_token):
        result = Request().send(url=select_product_change_status_page_info["url"],
                                method=select_product_change_status_page_info["method"],
                                data=select_product_change_status_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("产品状态变化管理详情接口")
    @pytest.mark.parametrize("select_product_change_status_detail_info",
                             select_product_change_status_detail_info)  # 产品状态变化管理详情接口
    def test_select_product_change_status_detail_info(self, select_product_change_status_detail_info, get_token):
        result = Request().send(url=select_product_change_status_detail_info["url"],
                                method=select_product_change_status_detail_info["method"],
                                data=select_product_change_status_detail_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
        write_yaml(Path.gsp_middle_data_path, "product_status_data", "data", result["body"]["obj"][0], None)

    @allure.title("产品状态变化新增接口")
    @pytest.mark.parametrize("create_product_change_status", create_product_change_status)  # 产品状态变化新增接口
    def test_create_product_change_status(self, create_product_change_status, get_token):
        detail_data = read_yaml(Path.gsp_middle_data_path, "product_status_data", "data")
        detail_data.pop("id")
        detail_data['changeQty'] = 0.001
        create_product_change_status['data']['dtList'][0] = detail_data
        create_product_change_status['data']['dtList'][0].update({
            "key": 0.17829811134581908,
            "approvalNumber": "国药准字氨糖",
            "changeTypeName": "合格转待处理",
            "originZoneName": "01零货库区",
            "originLotName": "LH0010",
            "_X_ROW_KEY": "row_95",
            "changeReason": 1
        })
        result = Request().send(url=create_product_change_status["url"],
                                method=create_product_change_status["method"],
                                data=create_product_change_status['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("产品状态变化审核接口")
    @pytest.mark.parametrize("audit_product_change_status",
                             audit_product_change_status)  # 产品状态变化审核接口
    def test_audit_product_change_status(self, audit_product_change_status, get_token):
        change_id = requests.post(
            url=read_yaml(Path.gsp_management_path, "select_product_change_status_page_info", "url"),
            json=read_yaml(Path.gsp_management_path, "select_product_change_status_page_info", "data"),
            headers=get_token,
        ).json()['obj'][0]['key']
        result = Request().send(url=audit_product_change_status["url"] + str(change_id),
                                method=audit_product_change_status["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("产品状态变化单查看接口")
    @pytest.mark.parametrize("product_change_status_detail_info",
                             product_change_status_detail_info)  # 产品状态变化单查看接口
    def test_product_change_status_detail_info(self, product_change_status_detail_info, get_token):
        change_id = requests.post(
            url=read_yaml(Path.gsp_management_path, "select_product_change_status_page_info", "url"),
            json=read_yaml(Path.gsp_management_path, "select_product_change_status_page_info", "data"),
            headers=get_token,
        ).json()['obj'][0]['key']
        result = Request().send(url=product_change_status_detail_info["url"] + str(change_id),
                                method=product_change_status_detail_info["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("养护管理列表查询接口")
    @pytest.mark.parametrize("select_yh_management_page_info",
                             select_yh_management_page_info)  # 养护管理列表查询接口
    def test_select_yh_management_page_info(self, select_yh_management_page_info, get_token):
        result = Request().send(url=select_yh_management_page_info["url"],
                                method=select_yh_management_page_info["method"],
                                data=select_yh_management_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("养护详情明细查询接口")
    @pytest.mark.parametrize("select_yh_management_detail_info",
                             select_yh_management_detail_info)  # 养护详情明细查询接口
    def test_select_yh_management_detail_info(self, select_yh_management_detail_info, get_token):
        result = Request().send(url=select_yh_management_detail_info["url"],
                                method=select_yh_management_detail_info["method"],
                                data=select_yh_management_detail_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
        write_yaml(Path.gsp_middle_data_path, "yh_management_data", "data", result["body"]["obj"][0], None)

    @allure.title("养护管理新增接口")
    @pytest.mark.parametrize("create_yh_management", create_yh_management)  # 养护管理新增接口
    def test_create_yh_management(self, create_yh_management, get_token):
        detail_data = read_yaml(Path.gsp_middle_data_path, "yh_management_data", "data")
        detail_data['key'] = 0.6014654118262268
        create_yh_management['data']['dtList'][0] = detail_data
        create_yh_management['data']['dtList'][0].update({
            "ownerName": None,
            "barcode": f"{detail_data['baseSku']['barcode']}",
            "skuName": f"{detail_data['baseSku']['skuName']}",
            "skuCategoryId": None,
            "skuCategoryName": "药品",
            "skuCategoryCode": None,
            "skuBigCategoryCode": None,
            "skuBigCategoryName": None,
            "spec": f"{detail_data['baseSku']['spec']}",
            "mainUnit": f"{detail_data['baseSku']['mainUnit']}",
            "perQty": detail_data['baseSku']['perQty'],
            "originCountry": f"{detail_data['baseSku']['originCountry']}",
            "drugForm": f"{detail_data['baseSku']['drugForm']}",
            "tradeName": f"{detail_data['baseSku']['tradeName']}",
            "approvalNumber": f"{detail_data['baseSku']['approvalNumber']}",
            "brandName": f"{detail_data['baseSku']['brandName']}",
            "mfgName": f"{detail_data['baseSku']['mfgName']}",
            "mfg": None,
            "permitHolder": f"{detail_data['baseSku']['permitHolder']}",
            "tempControl": f"{detail_data['baseSku']['tempControl']}",
            "validityDay": detail_data['baseSku']['validityDay'],
            "tempControlName": f"{detail_data['baseSku']['tempControlName']}",
            "tempMax": None,
            "tempMin": None,
            "mnemonicCode": None,
            "instrumentModel": None,
            "productionBatch": f"{detail_data['baseInvBatch']['productionBatch']}",
            "productionDate": f"{detail_data['baseInvBatch']['productionDate']}",
            "instoreDate": f"{detail_data['baseInvBatch']['instoreDate']}",
            "invalidDate": f"{detail_data['baseInvBatch']['invalidDate']}",
            "sterileInvaliDate": "",
            "sterileNo": "",
            "asnNo": None,
            "batchAsnNo": None,
            "po": None,
            "unitPrice": None,
            "spellBoxSign": None,
            "volume": None,
            "weight": None,
            "packQty": None,
            "_X_ROW_KEY": "row_675"
        }
        )
        result = Request().send(url=create_yh_management["url"],
                                method=create_yh_management["method"],
                                data=create_yh_management['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("养护任务单列表查询接口")
    @pytest.mark.parametrize("select_yh_mission_page_info",
                             select_yh_mission_page_info)  # 养护任务单列表查询接口
    def test_select_yh_mission_page_info(self, select_yh_mission_page_info, get_token):
        result = Request().send(url=select_yh_mission_page_info["url"],
                                method=select_yh_mission_page_info["method"],
                                data=select_yh_mission_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("养护任务详情明细查询接口")
    @pytest.mark.parametrize("select_yh_mission_detail_info",
                             select_yh_mission_detail_info)  # 养护任务详情明细查询接口
    def test_select_yh_mission_detail_info(self, select_yh_mission_detail_info, get_token):
        result = Request().send(url=select_yh_mission_detail_info["url"],
                                method=select_yh_mission_detail_info["method"],
                                data=select_yh_mission_detail_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
        write_yaml(Path.gsp_middle_data_path, "select_yh_mission_detail_data", "data", result["body"]["obj"][0], None)

    @allure.title("养护任务单创建接口")
    @pytest.mark.parametrize("create_yh_mission",
                             create_yh_mission)  # 养护任务单创建接口
    def test_create_yh_mission(self, create_yh_mission, get_token):
        detail_data = read_yaml(Path.gsp_middle_data_path, "select_yh_mission_detail_data", "data")
        create_yh_mission['data']['dtList'][0] = detail_data
        create_yh_mission['data']['dtList'][0].update({
            "ownerName": None,
            "barcode": f"{detail_data['baseSku']['barcode']}",
            "skuName": f"{detail_data['baseSku']['skuName']}",
            "skuCategoryId": None,
            "skuCategoryName": "药品",
            "skuCategoryCode": None,
            "skuBigCategoryCode": None,
            "skuBigCategoryName": None,
            "spec": f"{detail_data['baseSku']['spec']}",
            "mainUnit": f"{detail_data['baseSku']['mainUnit']}",
            "perQty": detail_data['baseSku']['perQty'],
            "originCountry": f"{detail_data['baseSku']['originCountry']}",
            "drugForm": f"{detail_data['baseSku']['drugForm']}",
            "tradeName": f"{detail_data['baseSku']['tradeName']}",
            "approvalNumber": f"{detail_data['baseSku']['approvalNumber']}",
            "brandName": f"{detail_data['baseSku']['brandName']}",
            "mfgName": f"{detail_data['baseSku']['mfgName']}",
            "mfg": None,
            "permitHolder": f"{detail_data['baseSku']['permitHolder']}",
            "tempControl": f"{detail_data['baseSku']['tempControl']}",
            "validityDay": detail_data['baseSku']['validityDay'],
            "tempControlName": f"{detail_data['baseSku']['tempControlName']}",
            "tempMax": None,
            "tempMin": None,
            "mnemonicCode": None,
            "instrumentModel": None,
            "productionBatch": f"{detail_data['baseInvBatch']['productionBatch']}",
            "productionDate": f"{detail_data['baseInvBatch']['productionDate']}",
            "instoreDate": f"{detail_data['baseInvBatch']['instoreDate']}",
            "invalidDate": f"{detail_data['baseInvBatch']['invalidDate']}",
            "sterileInvaliDate": "",
            "sterileNo": "",
            "asnNo": None,
            "batchAsnNo": None,
            "po": None,
            "unitPrice": None,
            "spellBoxSign": None,
            "volume": None,
            "weight": None,
            "packQty": None,
            "maintainConclusion": "JXXS",
            "_X_ROW_KEY": "row_675"})
        result = Request().send(url=create_yh_mission["url"],
                                method=create_yh_mission["method"],
                                data=create_yh_mission['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("产品养护档案查询接口")
    @pytest.mark.parametrize("select_yh_files",
                             select_yh_files)  # 产品养护档案查询接口
    def test_select_yh_files(self, select_yh_files, get_token):
        result = Request().send(url=select_yh_files["url"],
                                method=select_yh_files["method"],
                                data=select_yh_files['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("质量复检通知单列表查询接口")
    @pytest.mark.parametrize("select_check_quality_page_info",
                             select_check_quality_page_info)  # 质量复检通知单列表查询接口
    def test_select_check_quality_page_info(self, select_check_quality_page_info, get_token):
        result = Request().send(url=select_check_quality_page_info["url"],
                                method=select_check_quality_page_info["method"],
                                data=select_check_quality_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("质量复检通知单详情明细查询接口")
    @pytest.mark.parametrize("select_check_quality_detail_info",
                             select_check_quality_detail_info)  # 质量复检通知单详情明细查询接口
    def test_select_check_quality_detail_info(self, select_check_quality_detail_info, get_token):
        result = Request().send(url=select_check_quality_detail_info["url"],
                                method=select_check_quality_detail_info["method"],
                                data=select_check_quality_detail_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
        write_yaml(Path.gsp_middle_data_path, "select_check_quality_detail_data", "data", result["body"]["obj"][0],
                   None)

    @allure.title("质量复检通知单新增接口")
    @pytest.mark.parametrize("create_check_quality",
                             create_check_quality)  # 质量复检通知单新增接口
    def test_create_check_quality(self, create_check_quality, get_token):
        detail_data = read_yaml(Path.gsp_middle_data_path, "select_check_quality_detail_data", "data")
        detail_data.pop("id")
        create_check_quality['data']['dtList'][0] = detail_data
        create_check_quality['data']['dtList'][0].update({
            "skuId": f"{detail_data['skuPo']['skuId']}",
            "skuCode": f"{detail_data['skuPo']['skuCode']}",
            "barcode": f"{detail_data['skuPo']['barcode']}",
            "skuName": f"{detail_data['skuPo']['skuName']}",
            "skuCategoryId": None,
            "skuCategoryName": "药品",
            "skuCategoryCode": None,
            "skuBigCategoryCode": None,
            "skuBigCategoryName": None,
            "spec": f"{detail_data['skuPo']['spec']}",
            "mainUnit": f"{detail_data['skuPo']['mainUnit']}",
            "perQty": detail_data['skuPo']['perQty'],
            "originCountry": f"{detail_data['skuPo']['originCountry']}",
            "drugForm": f"{detail_data['skuPo']['drugForm']}",
            "tradeName": f"{detail_data['skuPo']['tradeName']}",
            "approvalNumber": f"{detail_data['skuPo']['approvalNumber']}",
            "brandName": f"{detail_data['skuPo']['brandName']}",
            "mfgName": f"{detail_data['skuPo']['mfgName']}",
            "mfg": None,
            "permitHolder": f"{detail_data['skuPo']['permitHolder']}",
            "tempControl": f"{detail_data['skuPo']['tempControl']}",
            "validityDay": detail_data['skuPo']['validityDay'],
            "tempControlName": f"{detail_data['skuPo']['tempControlName']}",
            "tempMax": None,
            "tempMin": None,
            "mnemonicCode": None,
            "instrumentModel": None,
            "productionBatch": f"{detail_data['baseInvBatch']['productionBatch']}",
            "productionDate": f"{detail_data['baseInvBatch']['productionDate']}",
            "instoreDate": f"{detail_data['baseInvBatch']['instoreDate']}",
            "invalidDate": f"{detail_data['baseInvBatch']['invalidDate']}",
            "sterileInvaliDate": "",
            "sterileNo": "",
            "batchAsnNo": None,
            "po": None,
            "unitPrice": None,
            "spellBoxSign": None,
            "volume": None,
            "weight": None,
            "packQty": None,
            "maintainConclusion": "JXXS",
            "_X_ROW_KEY": "row_675",
            "batchNo": f"{detail_data['baseInvBatch']['batchNo']}",
            "stockInfoId": f"{detail_data['key']}",
            "stockId": f"{detail_data['key']}",
            "recheckQty": "0.001",
            "recheckReason": "JXQ"
        })
        result = Request().send(url=create_check_quality["url"],
                                method=create_check_quality["method"],
                                data=create_check_quality['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("质量复检通知单查询接口")
    @pytest.mark.parametrize("select_check_quality_detail",
                             select_check_quality_detail)  # 质量复检通知单查询接口
    def test_select_check_quality_detail(self, select_check_quality_detail, get_token):
        detail_id = requests.post(
            url=read_yaml(Path.gsp_management_path, "select_check_quality_page_info", "url"),
            json=read_yaml(Path.gsp_management_path, "select_check_quality_page_info", "data"),
            headers=get_token
        ).json()['obj'][0]['key']
        result = Request().send(url=select_check_quality_detail["url"] + str(detail_id),
                                method=select_check_quality_detail["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("质量复检通知单审核接口")
    @pytest.mark.parametrize("audit_check_quality",
                             audit_check_quality)  # 质量复检通知单审核接口
    def test_audit_check_quality(self, audit_check_quality, get_token):
        detail_id = requests.post(
            url=read_yaml(Path.gsp_management_path, "select_check_quality_page_info", "url"),
            json=read_yaml(Path.gsp_management_path, "select_check_quality_page_info", "data"),
            headers=get_token
        ).json()['obj'][0]['key']
        result = Request().send(url=audit_check_quality["url"] + str(detail_id),
                                method=audit_check_quality["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("质量复检审核列表查询接口")
    @pytest.mark.parametrize("select_audit_quality_list_info",
                             select_audit_quality_list_info)  # 质量复检审核列表查询接口
    def test_select_select_audit_quality_list_info(self, select_audit_quality_list_info, get_token):
        result = Request().send(url=select_audit_quality_list_info["url"],
                                method=select_audit_quality_list_info["method"],
                                data=select_audit_quality_list_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("质量复检审核详情明细查询接口")
    @pytest.mark.parametrize("select_audit_quality_detail_info",
                             select_audit_quality_detail_info)  # 质量复检审核详情明细查询接口
    def test_select_audit_quality_detail_info(self, select_audit_quality_detail_info, get_token):
        detail_id = requests.post(
            url=read_yaml(Path.gsp_management_path, "select_audit_quality_list_info", "url"),
            json=read_yaml(Path.gsp_management_path, "select_audit_quality_list_info", "data"),
            headers=get_token
        ).json()['obj'][0]['key']
        result = Request().send(url=select_audit_quality_detail_info["url"] + str(detail_id),
                                method=select_audit_quality_detail_info["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
        write_yaml(Path.gsp_middle_data_path, "select_audit_quality_detail_data", "data",
                   result["body"]["obj"]['entity'],
                   None)

    @allure.title("质量复检审核接口")
    @pytest.mark.parametrize("create_audit_quality",
                             create_audit_quality)  # 质量复检审核接口
    def test_create_audit_quality(self, create_audit_quality, get_token):
        detail_data = read_yaml(Path.gsp_middle_data_path, "select_audit_quality_detail_data", "data")
        detail_data['dtList'][0]['checkResult'] = "NG"
        detail_data['dtList'][0]['dealMsg'] = "BS"
        detail_data['dtList'][0]['dealMsgName'] = "报损"
        detail_data['dtList'][0].update({
            "ownerName": None,
            "barcode": f"{detail_data['dtList'][0]['skuPo']['barcode']}",
            "skuName": f"{detail_data['dtList'][0]['skuPo']['skuName']}",
            "skuCategoryId": None,
            "skuCategoryName": None,
            "skuCategoryCode": None,
            "skuBigCategoryCode": None,
            "skuBigCategoryName": None,
            "spec": f"{detail_data['dtList'][0]['skuPo']['spec']}",
            "mainUnit": f"{detail_data['dtList'][0]['skuPo']['mainUnit']}",
            "perQty": detail_data['dtList'][0]['skuPo']['perQty'],
            "originCountry": f"{detail_data['dtList'][0]['skuPo']['originCountry']}",
            "drugForm": "_",
            "tradeName": f"{detail_data['dtList'][0]['skuPo']['tradeName']}",
            "approvalNumber": f"{detail_data['dtList'][0]['skuPo']['approvalNumber']}",
            "brandName": "",
            "mfgName": f"{detail_data['dtList'][0]['skuPo']['mfgName']}",
            "mfg": None,
            "permitHolder": "",
            "tempControl": f"{detail_data['dtList'][0]['skuPo']['tempControl']}",
            "validityDay": 0,
            "tempControlName": f"{detail_data['dtList'][0]['skuPo']['tempControlName']}",
            "tempMax": None,
            "tempMin": None,
            "mnemonicCode": None,
            "instrumentModel": None,
            "productionBatch": f"{detail_data['dtList'][0]['invBatchPo']['productionBatch']}",
            "productionDate": f"{detail_data['dtList'][0]['invBatchPo']['productionDate']}",
            "instoreDate": f"{detail_data['dtList'][0]['invBatchPo']['instoreDate']}",
            "invalidDate": f"{detail_data['dtList'][0]['invBatchPo']['invalidDate']}",
            "sterileInvaliDate": "",
            "sterileNo": "",
            "asnNo": None,
            "batchAsnNo": None,
            "po": None,
            "unitPrice": None,
            "spellBoxSign": None,
            "volume": None,
            "weight": None,
            "packQty": None,
            "_X_ROW_KEY": "row_246"
        })
        detail_data.update({
            "rowIndex": 0,
            "delDtIds": []
        })
        print(detail_data)
        result = Request().send(url=create_audit_quality["url"],
                                method=create_audit_quality["method"],
                                data=detail_data,
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("质量复检审核完成接口")
    @pytest.mark.parametrize("audit_quality_audit",
                             audit_quality_audit)  # 质量复检审核完成接口
    def test_audit_quality_audit(self, audit_quality_audit, get_token):
        detail_id = requests.post(
            url=read_yaml(Path.gsp_management_path, "select_audit_quality_list_info", "url"),
            json=read_yaml(Path.gsp_management_path, "select_audit_quality_list_info", "data"),
            headers=get_token
        ).json()['obj'][0]['key']
        result = Request().send(url=audit_quality_audit["url"] + str(detail_id),
                                method=audit_quality_audit["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("不合格产品报损列表查询接口")
    @pytest.mark.parametrize("select_bhg_product_page_info",
                             select_bhg_product_page_info)  # 不合格产品报损列表查询接口
    def test_select_bhg_product_page_info(self, select_bhg_product_page_info, get_token):
        result = Request().send(url=select_bhg_product_page_info["url"],
                                method=select_bhg_product_page_info["method"],
                                data=select_bhg_product_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("不合格产品详情明细查询接口")
    @pytest.mark.parametrize("select_bhg_product_detail_info",
                             select_bhg_product_detail_info)  # 不合格产品详情明细查询接口
    def test_select_bhg_product_detail_info(self, select_bhg_product_detail_info, get_token):
        result = Request().send(url=select_bhg_product_detail_info["url"],
                                method=select_bhg_product_detail_info["method"],
                                data=select_bhg_product_detail_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
        write_yaml(Path.gsp_middle_data_path, "select_bhg_product_detail_data", "data",
                   result["body"]["obj"][0],
                   None)

    @allure.title("不合格产品新增接口")
    @pytest.mark.parametrize("create_bhg_product",
                             create_bhg_product)  # 不合格产品新增接口
    def test_create_bhg_product(self, create_bhg_product, get_token):
        detail_data = read_yaml(Path.gsp_middle_data_path, "select_bhg_product_detail_data", "data")
        create_bhg_product['data']['dtList'][0] = detail_data
        create_bhg_product['data']['dtList'][0]['sourceCarrierId'] = "1771520756486656"
        create_bhg_product['data']['dtList'][0]['sourcePrice'] = 1
        create_bhg_product['data']['dtList'][0].update({
            "key": 0.1285738026283727,
            "approvalNumber": f"{detail_data['approveNo']}",
            "originZoneName": f"{detail_data['zoneName']}",
            "originLotName": f"{detail_data['lotCode']}",
            "packFactoryName": None,
            "stockId": detail_data['id'],
            "_X_ROW_KEY": "row_132",
            "badQty": f"{detail_data['usableQty']}",
            "compensationAmount": f"{detail_data['usableQty']}",
            "badReason": "GXQ",
            "dealMsg": "BS"
        })
        create_bhg_product['data']['dtList'][0].pop("id")
        result = Request().send(url=create_bhg_product["url"],
                                method=create_bhg_product["method"],
                                data=create_bhg_product['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("不合格产品审核接口")
    @pytest.mark.parametrize("bhg_product_audit",
                             bhg_product_audit)  # 不合格产品审核接口
    def test_bhg_product_audit(self, bhg_product_audit, get_token):
        detail_data = read_yaml(Path.gsp_management_path, "select_bhg_product_page_info", "data")
        detail_data['ncrStatus'] = "NEW"
        detail_id = requests.post(
            url=read_yaml(Path.gsp_management_path, "select_bhg_product_page_info", "url"),
            json=detail_data,
            headers=get_token
        ).json()['obj'][0]['key']
        result = Request().send(url=bhg_product_audit["url"] + str(detail_id),
                                method=bhg_product_audit["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("erp审核不合格产品接口")
    @pytest.mark.parametrize("erp_audit_bhg_product",
                             erp_audit_bhg_product)  # erp审核不合格产品接口
    def test_erp_audit_bhg_product(self, erp_audit_bhg_product, get_token):
        detail_data = read_yaml(Path.gsp_management_path, "select_bhg_product_page_info", "data")
        detail_data['ncrStatus'] = "SHZ"
        detail_id = requests.post(
            url=read_yaml(Path.gsp_management_path, "select_bhg_product_page_info", "url"),
            json=detail_data,
            headers=get_token
        ).json()['obj'][0]
        erp_audit_bhg_product['data']['ncrNo'] = detail_id['ncrNo']
        erp_audit_bhg_product['data']['dtList'][0]['agreeQty'] = \
            read_yaml(Path.gsp_middle_data_path, "select_bhg_product_detail_data", "data")['usableQty']
        result = Request().send(url=erp_audit_bhg_product["url"],
                                method=erp_audit_bhg_product["method"],
                                data=erp_audit_bhg_product['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("PDA报损下架接口")
    @pytest.mark.parametrize("bhg_down_shelf",
                             bhg_down_shelf)  # PDA报损下架接口
    def test_bhg_down_shelf(self, bhg_down_shelf, get_token):
        detail_data = read_yaml(Path.gsp_management_path, "select_bhg_product_page_info", "data")
        detail_data['ncrStatus'] = "SHWC"
        detail_id = requests.post(
            url=read_yaml(Path.gsp_management_path, "select_bhg_product_page_info", "url"),
            json=detail_data,
            headers=get_token
        ).json()['obj'][0]
        bhg_down_shelf['data']['ncrNo'] = detail_id['ncrNo']
        bhg_down_shelf['data']['perQty'] = \
            read_yaml(Path.gsp_middle_data_path, "select_bhg_product_detail_data", "data")['perQty']
        bhg_down_shelf['data']['packageAttr'] = \
            read_yaml(Path.gsp_middle_data_path, "select_bhg_product_detail_data", "data")['packageAttr']
        bhg_down_shelf['data']['bsQty'] = \
            read_yaml(Path.gsp_middle_data_path, "select_bhg_product_detail_data", "data")['usableQty']
        bhg_down_shelf['data']['batchNo'] = \
            read_yaml(Path.gsp_middle_data_path, "select_bhg_product_detail_data", "data")['batchNo']
        bhg_down_shelf['data']['lotCode'] = \
            read_yaml(Path.gsp_middle_data_path, "select_bhg_product_detail_data", "data")['lotName']
        result = Request().send(url=bhg_down_shelf["url"],
                                method=bhg_down_shelf["method"],
                                data=bhg_down_shelf['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("销毁作业列表查询接口")
    @pytest.mark.parametrize("select_destroy_product_page_info",
                             select_destroy_product_page_info)  # 销毁作业列表查询接口
    def test_select_destroy_product_page_info(self, select_destroy_product_page_info, get_token):
        result = Request().send(url=select_destroy_product_page_info["url"],
                                method=select_destroy_product_page_info["method"],
                                data=select_destroy_product_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("销毁作业详情明细查询接口")
    @pytest.mark.parametrize("select_destroy_product_detail_info",
                             select_destroy_product_detail_info)  # 销毁作业详情明细查询接口
    def test_select_destroy_product_detail_info(self, select_destroy_product_detail_info, get_token):
        result = Request().send(url=select_destroy_product_detail_info["url"],
                                method=select_destroy_product_detail_info["method"],
                                data=select_destroy_product_detail_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
        assert result['body']['obj'] is not None
        write_yaml(Path.gsp_middle_data_path, "select_destroy_product_detail_data", "data",
                   result["body"]["obj"][0],
                   None)

    @allure.title("销毁作业新增接口")
    @pytest.mark.parametrize("create_destroy_product",
                             create_destroy_product)  # 销毁作业新增接口
    def test_create_destroy_product(self, create_destroy_product, get_token):
        detail_data = read_yaml(Path.gsp_middle_data_path, "select_destroy_product_detail_data", "data")
        detail_data.pop("mfg")
        detail_data.pop("id")
        create_destroy_product['data']['destroyInfoDtReqList'][0] = detail_data
        create_destroy_product['data']['destroyInfoDtReqList'][0].update({
            "mfg": f"{detail_data['skuPo']['mfgName']}",
            "productionBatch": f"{detail_data['invBatchPo']['productionBatch']}",
            "productionDate": f"{detail_data['invBatchPo']['productionDate']}",
            "instoreDate": f"{detail_data['invBatchPo']['instoreDate']}",
            "invalidDate": f"{detail_data['invBatchPo']['invalidDate']}",
            "batchAsnNo": None,
            "po": None,
            "unitPrice": None,
            "spellBoxSign": None,
            "volume": None,
            "weight": None,
            "packQty": None,
            "ownerName": None,
            "barcode": None,
            "skuName": f"{detail_data['skuPo']['skuName']}",
            "skuCategoryId": None,
            "skuCategoryName": None,
            "skuCategoryCode": None,
            "skuBigCategoryCode": None,
            "skuBigCategoryName": None,
            "spec": f"{detail_data['skuPo']['spec']}",
            "mainUnit": f"{detail_data['skuPo']['mainUnit']}",
            "tradeName": f"{detail_data['skuPo']['tradeName']}",
            "brandName": "",
            "mfgName": f"{detail_data['skuPo']['mfgName']}",
            "validityDay": None,
            "tempMax": None,
            "tempMin": None,
            "mnemonicCode": None,
            "instrumentModel": None,
            "ncrDtId": f"{detail_data['key']}",
            "destroyQty": f"{detail_data['badQty']}",
            "destroyReason": "GXQ",
            "_X_ROW_KEY": "row_52"
        })
        result = Request().send(url=create_destroy_product["url"],
                                method=create_destroy_product["method"],
                                data=create_destroy_product['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("销毁作业一次审核接口")
    @pytest.mark.parametrize("audit_destroy_product",
                             audit_destroy_product)  # 销毁作业一次审核接口
    def test_audit_destroy_productt(self, audit_destroy_product, get_token):
        detail_id = requests.post(
            url=read_yaml(Path.gsp_management_path, "select_destroy_product_page_info", "url"),
            json=read_yaml(Path.gsp_management_path, "select_destroy_product_page_info", "data"),
            headers=get_token
        ).json()['obj'][0]['key']
        result = Request().send(url=audit_destroy_product["url"] + str(detail_id),
                                method=audit_destroy_product["method"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("销毁作业二次审核接口")
    @pytest.mark.parametrize("second_audit_destroy_product",
                             second_audit_destroy_product)  # 销毁作业一次审核接口
    def test_second_audit_destroy_product(self, second_audit_destroy_product):
        url = read_yaml(Path.config_file_path, 'login_data', 'url')
        data = {
            "userNo": "lihongbin",
            "pwd": "lhx7758521",
            "platForm": "app",
            "companyCode": "ZHQC",
            "whId": 1,
            "warehouseId": "",
            "haveWarehouse": 1,
            "clientId": "iowtb-new",
            "userLanguage": "zh-CN"
        }
        res = requests.post(url=url, json=data, headers={'Content-Type': 'application/json'})
        token = res.json()['obj']['token']
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        detail_id = requests.post(
            url=read_yaml(Path.gsp_management_path, "select_destroy_product_page_info", "url"),
            json=read_yaml(Path.gsp_management_path, "select_destroy_product_page_info", "data"),
            headers=headers
        ).json()['obj'][0]['key']
        result = Request().send(url=second_audit_destroy_product["url"] + str(detail_id),
                                method=second_audit_destroy_product["method"],
                                headers=headers)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("近效期催销列表接口")
    @pytest.mark.parametrize("select_near_expire_date_page_info",
                             select_near_expire_date_page_info)  # 近效期催销列表接口
    def test_select_near_expire_date_page_info(self, select_near_expire_date_page_info, get_token):
        result = Request().send(url=select_near_expire_date_page_info["url"],
                                method=select_near_expire_date_page_info["method"],
                                data=select_near_expire_date_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("滞销催销列表接口")
    @pytest.mark.parametrize("select_unsalable_page_info",
                             select_unsalable_page_info)  # 滞销催销列表接口
    def test_select_unsalable_page_info(self, select_unsalable_page_info, get_token):
        result = Request().send(url=select_unsalable_page_info["url"],
                                method=select_unsalable_page_info["method"],
                                data=select_unsalable_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("滞销催销详情明细查询接口")
    @pytest.mark.parametrize("select_unsalable_detail_info",
                             select_unsalable_detail_info)  # 滞销催销详情明细查询接口
    def test_select_unsalable_detail_info(self, select_unsalable_detail_info, get_token):
        result = Request().send(url=select_unsalable_detail_info["url"],
                                method=select_unsalable_detail_info["method"],
                                data=select_unsalable_detail_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
        write_yaml(Path.gsp_middle_data_path, "select_unsalable_detail_data", "data",
                   result["body"]["obj"][0],
                   None)

    @allure.title("滞销催销新增接口")
    @pytest.mark.parametrize("create_unsalable_data",
                             create_unsalable_data)  # 滞销催销新增接口
    def test_create_unsalable_data(self, create_unsalable_data, get_token):
        detail_data = read_yaml(Path.gsp_middle_data_path, "select_unsalable_detail_data", "data")
        create_unsalable_data['data']['dtList'][0] = detail_data
        create_unsalable_data['data']['dtList'][0].update({
            "ownerName": None,
            "barcode": f"{detail_data['skuPo']['barcode']}",
            "skuName": f"{detail_data['skuPo']['skuName']}",
            "skuCategoryId": None,
            "skuCategoryName": None,
            "skuCategoryCode": None,
            "skuBigCategoryCode": None,
            "skuBigCategoryName": None,
            "spec": f"{detail_data['skuPo']['spec']}",
            "mainUnit": f"{detail_data['skuPo']['mainUnit']}",
            "perQty": f"{detail_data['skuPo']['perQty']}",
            "originCountry": f"{detail_data['skuPo']['originCountry']}",
            "drugForm": "_",
            "tradeName": f"{detail_data['skuPo']['tradeName']}",
            "approvalNumber": f"{detail_data['skuPo']['approvalNumber']}",
            "brandName": "",
            "mfgName": f"{detail_data['skuPo']['mfgName']}",
            "mfg": None,
            "permitHolder": "",
            "tempControl": f"{detail_data['skuPo']['tempControl']}",
            "validityDay": None,
            "tempControlName": f"{detail_data['skuPo']['tempControlName']}",
            "tempMax": None,
            "tempMin": None,
            "mnemonicCode": None,
            "instrumentModel": None,
            "productionBatch": f"{detail_data['invBatchPo']['productionBatch']}",
            "productionDate": f"{detail_data['invBatchPo']['productionDate']}",
            "instoreDate": f"{detail_data['invBatchPo']['instoreDate']}",
            "invalidDate": f"{detail_data['invBatchPo']['invalidDate']}",
            "sterileInvaliDate": "",
            "sterileNo": "",
            "asnNo": None,
            "batchAsnNo": None,
            "po": None,
            "unitPrice": None,
            "spellBoxSign": None,
            "volume": None,
            "weight": None,
            "packQty": None,
            "_X_ROW_KEY": "row_227"
        })
        result = Request().send(url=create_unsalable_data["url"],
                                method=create_unsalable_data["method"],
                                data=create_unsalable_data['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("滞销催销报表查询接口")
    @pytest.mark.parametrize("select_unsalable_list_page_info",
                             select_unsalable_list_page_info)  # 滞销催销报表查询接口
    def test_select_unsalable_list_page_info(self, select_unsalable_list_page_info, get_token):
        result = Request().send(url=select_unsalable_list_page_info["url"],
                                method=select_unsalable_list_page_info["method"],
                                data=select_unsalable_list_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"

    @allure.title("即时库存查询接口")
    @pytest.mark.parametrize("select_immediate_list_page_info",
                             select_immediate_list_page_info)  # 即时库存查询接口
    def test_select_immediate_list_page_info(self, select_immediate_list_page_info, get_token):
        result = Request().send(url=select_immediate_list_page_info["url"],
                                method=select_immediate_list_page_info["method"],
                                data=select_immediate_list_page_info['data'],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"]["msg"] == "成功"
