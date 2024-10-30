import pytest
from config.path import *
from utils.get_yaml_data import *
from utils.requests_util import Request
from utils.log import logger
from utils.mysql_util import CommonDatabase
import allure


class TestBaseData:
    base_warehouse = read_yaml(Path.base_data_path, "base_warehouse_data")
    base_warehouse_inside = read_yaml(Path.base_data_path, "base_warehouse_inside")
    base_owner = read_yaml(Path.base_data_path, "base_owner_data")
    base_warehouse_location = read_yaml(Path.base_data_path, "base_warehouse_location")
    base_warehouse_temporary = read_yaml(Path.base_data_path, "base_warehouse_temporary")
    base_user_data = read_yaml(Path.base_data_path, "base_user_data")
    base_department_data = read_yaml(Path.base_data_path, "base_department_data")
    base_person_data = read_yaml(Path.base_data_path, "base_person_data")
    base_department_relationship_data = read_yaml(Path.base_data_path, "base_department_relationship_data")
    base_customer_data = read_yaml(Path.base_data_path, "base_customer_data")
    base_supplier_data = read_yaml(Path.base_data_path, "base_supplier_data")
    base_shop_data = read_yaml(Path.base_data_path, "base_shop_data")
    base_product_data = read_yaml(Path.base_data_path, "base_product_data")
    base_management_data = read_yaml(Path.base_data_path, "base_management_data")
    base_commodity_data = read_yaml(Path.base_data_path, "base_commodity_data")
    base_supervise_data = read_yaml(Path.base_data_path, "base_supervise_data")
    base_warehouse_container = read_yaml(Path.base_data_path, "base_warehouse_container")
    base_consignment_data = read_yaml(Path.base_data_path, "base_consignment_data")
    base_erp_consignment_data = read_yaml(Path.base_data_path, "base_erp_consignment_data")
    base_deliver_data = read_yaml(Path.base_data_path, "base_deliver_data")
    base_car_data = read_yaml(Path.base_data_path, "base_car_data")
    base_create_customer = read_yaml(Path.base_data_path, "base_create_customer")
    base_create_supplier = read_yaml(Path.base_data_path, "base_create_supplier")
    base_create_shop = read_yaml(Path.base_data_path, "base_create_shop")
    base_create_product_company = read_yaml(Path.base_data_path, "base_create_product_company")
    base_create_commodity_range = read_yaml(Path.base_data_path, "base_create_commodity_range")
    base_delete_commodity_range = read_yaml(Path.base_data_path, "base_delete_commodity_range")
    base_create_commodity = read_yaml(Path.base_data_path, "base_create_commodity")
    base_delete_commodity = read_yaml(Path.base_data_path, "base_delete_commodity")
    base_commodity_details = read_yaml(Path.base_data_path, "base_commodity_details")
    base_update_details = read_yaml(Path.base_data_path, "base_update_details")
    base_commodity_supervise_details = read_yaml(Path.base_data_path, "base_commodity_supervise_details")
    base_commodity_supervise_update = read_yaml(Path.base_data_path, "base_commodity_supervise_update")
    base_create_container = read_yaml(Path.base_data_path, "base_create_container")
    base_delete_container = read_yaml(Path.base_data_path, "base_delete_container")
    base_create_slide = read_yaml(Path.base_data_path, "base_create_slide")
    base_delete_slide = read_yaml(Path.base_data_path, "base_delete_slide")
    base_create_pick_container = read_yaml(Path.base_data_path, "base_create_pick_container")
    base_delete_pick_container = read_yaml(Path.base_data_path, "base_delete_pick_container")
    base_create_work_container = read_yaml(Path.base_data_path, "base_create_work_container")
    base_delete_work_container = read_yaml(Path.base_data_path, "base_delete_work_container")
    base_create_consignment = read_yaml(Path.base_data_path, "base_create_consignment")
    base_create_erp_consignment = read_yaml(Path.base_data_path, "base_create_erp_consignment")
    base_create_road_data = read_yaml(Path.base_data_path, "base_create_road_data")
    base_delete_road_data = read_yaml(Path.base_data_path, "base_delete_road_data")
    base_create_consignment_data = read_yaml(Path.base_data_path, "base_create_consignment_data")
    base_delete_consignment_data = read_yaml(Path.base_data_path, "base_delete_consignment_data")
    base_create_driver_data = read_yaml(Path.base_data_path, "base_create_driver_data")
    base_delete_driver_data = read_yaml(Path.base_data_path, "base_delete_driver_data")
    base_create_car_data = read_yaml(Path.base_data_path, "base_create_car_data")
    base_delete_car_data = read_yaml(Path.base_data_path, "base_delete_car_data")

    @allure.title("仓库列表查询接口")
    @pytest.mark.parametrize("warehouse_data", base_warehouse)  # 测试获取仓库列表接口
    def test_warehouse_data(self, warehouse_data, get_token):
        result = Request().send(url=warehouse_data["url"], method=warehouse_data["method"], data=warehouse_data["data"],
                                headers=get_token)
        logger.info([warehouse_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("库内移动规则查询接口")
    @pytest.mark.parametrize("warehouse_inside", base_warehouse_inside)  # 测试获取库内移动规则
    def test_warehouse_inside(self, warehouse_inside, get_token):
        result = Request().send(url=warehouse_inside["url"], method=warehouse_inside["method"],
                                data=warehouse_inside["data"],
                                headers=get_token)
        logger.info([warehouse_inside['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("货主列表查询接口")
    @pytest.mark.parametrize("owner_data", base_owner)  # 测试获取货主列表数据
    def test_warehouse_owner(self, owner_data, get_token):
        result = Request().send(url=owner_data["url"], method=owner_data["method"],
                                data=owner_data["data"],
                                headers=get_token)
        logger.info([owner_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("维护库房库区资料接口")
    @pytest.mark.parametrize("warehouse_location", base_warehouse_location)  # 测试库房库区列表数据
    def test_warehouse_location(self, warehouse_location, get_token):
        result = Request().send(url=warehouse_location["url"], method=warehouse_location["method"],
                                data=warehouse_location["data"],
                                headers=get_token)
        logger.info([warehouse_location['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("暂存区列表查询接口")
    @pytest.mark.parametrize("warehouse_temporary", base_warehouse_temporary)  # 测试暂存区列表查询
    def test_warehouse_temporary(self, warehouse_temporary, get_token):
        result = Request().send(url=warehouse_temporary["url"], method=warehouse_temporary["method"],
                                data=warehouse_temporary["data"],
                                headers=get_token)
        logger.info([warehouse_temporary['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("用户数据列表查询接口")
    @pytest.mark.parametrize("user_data", base_user_data)  # 测试获取用户数据
    def test_warehouse_user(self, user_data, get_token):
        result = Request().send(url=user_data["url"], method=user_data["method"],
                                data=user_data["data"],
                                headers=get_token)
        logger.info([user_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("部门列表查询接口")
    @pytest.mark.parametrize("department_data", base_department_data)  # 测试获取部门数据
    def test_warehouse_department(self, department_data, get_token):
        result = Request().send(url=department_data["url"], method=department_data["method"],
                                data=department_data["data"],
                                headers=get_token)
        logger.info([department_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("人员安排列表查询接口")
    @pytest.mark.parametrize("person_data", base_person_data)  # 测试获取人员安排数据
    def test_warehouse_person(self, person_data, get_token):
        result = Request().send(url=person_data["url"], method=person_data["method"],
                                data=person_data["data"],
                                headers=get_token)
        logger.info([person_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("部门关系列表查询接口")
    @pytest.mark.parametrize("relationship_data", base_department_relationship_data)  # 测试部门关系
    def test_warehouse_department_relationship(self, relationship_data, get_token):
        result = Request().send(url=relationship_data["url"], method=relationship_data["method"],
                                data=relationship_data["data"],
                                headers=get_token)
        logger.info([relationship_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("客户列表查询接口")
    @pytest.mark.parametrize("customer_data", base_customer_data)  # 测试获取客户数据
    def test_warehouse_customer(self, customer_data, get_token):
        result = Request().send(url=customer_data["url"], method=customer_data["method"],
                                data=customer_data["data"],
                                headers=get_token)
        logger.info([customer_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("供应商列表查询接口")
    @pytest.mark.parametrize("supplier_data", base_supplier_data)  # 测试获取供应商数据
    def test_warehouse_supplier(self, supplier_data, get_token):
        result = Request().send(url=supplier_data["url"], method=supplier_data["method"],
                                data=supplier_data["data"],
                                headers=get_token)
        logger.info([supplier_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("店铺列表查询接口")
    @pytest.mark.parametrize("shop_data", base_shop_data)  # 测试获取店铺数据
    def test_warehouse_shop(self, shop_data, get_token):
        result = Request().send(url=shop_data["url"], method=shop_data["method"],
                                data=shop_data["data"],
                                headers=get_token)
        logger.info([shop_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("生产商列表查询接口")
    @pytest.mark.parametrize("product_data", base_product_data)  # 测试获取生产商数据
    def test_warehouse_product(self, product_data, get_token):
        result = Request().send(url=product_data["url"], method=product_data["method"],
                                data=product_data["data"],
                                headers=get_token)
        logger.info([product_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("经营范围列表查询接口")
    @pytest.mark.parametrize("management_data", base_management_data)  # 测试获取经营范围数据
    def test_warehouse_management(self, management_data, get_token):
        result = Request().send(url=management_data["url"], method=management_data["method"],
                                data=management_data["data"],
                                headers=get_token)
        logger.info([management_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("商品数据列表查询接口")
    @pytest.mark.parametrize("commodity_data", base_commodity_data)  # 测试获取商品数据
    def test_warehouse_commodity(self, commodity_data, get_token):
        result = Request().send(url=commodity_data["url"], method=commodity_data["method"],
                                data=commodity_data["data"],
                                headers=get_token)
        logger.info([commodity_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("商品监管数据列表查询接口")
    @pytest.mark.parametrize("supervise_data", base_supervise_data)  # 测试获取商品监管数据
    def test_warehouse_supervise(self, supervise_data, get_token):
        result = Request().send(url=supervise_data["url"], method=supervise_data["method"],
                                data=supervise_data["data"],
                                headers=get_token)
        logger.info([supervise_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("仓储容器列表查询接口")
    @pytest.mark.parametrize("container_data", base_warehouse_container)  # 测试获取仓储容器数据
    def test_warehouse_container(self, container_data, get_token):
        result = Request().send(url=container_data["url"], method=container_data["method"],
                                data=container_data["data"],
                                headers=get_token)
        logger.info([container_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("托运公司列表查询接口")
    @pytest.mark.parametrize("consignment_data", base_consignment_data)  # 测试获取托运公司数据
    def test_warehouse_consignment(self, consignment_data, get_token):
        result = Request().send(url=consignment_data["url"], method=consignment_data["method"],
                                data=consignment_data["data"],
                                headers=get_token)
        logger.info([consignment_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("erp承运商列表查询接口")
    @pytest.mark.parametrize("erp_consignment_data", base_erp_consignment_data)  # 测试获取erp承运商数据
    def test_warehouse_erp_consignment(self, erp_consignment_data, get_token):
        result = Request().send(url=erp_consignment_data["url"], method=erp_consignment_data["method"],
                                data=erp_consignment_data["data"],
                                headers=get_token)
        logger.info([erp_consignment_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("司机列表查询接口")
    @pytest.mark.parametrize("deliver_data", base_deliver_data)  # 测试获取司机数据
    def test_warehouse_deliver(self, deliver_data, get_token):
        result = Request().send(url=deliver_data["url"], method=deliver_data["method"],
                                data=deliver_data["data"],
                                headers=get_token)
        logger.info([deliver_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("车辆列表查询接口")
    @pytest.mark.parametrize("car_data", base_car_data)  # 测试获取车辆数据
    def test_warehouse_car(self, car_data, get_token):
        result = Request().send(url=car_data["url"], method=car_data["method"],
                                data=car_data["data"],
                                headers=get_token)
        logger.info([car_data['title'], result])
        assert result['code'] == 200 and result["body"] is not None

    @allure.title("新增客户接口")
    @pytest.mark.parametrize("creat_customer", base_create_customer)  # 测试新增客户数据
    def test_create_customer(self, creat_customer, get_token):
        result = Request().send(url=creat_customer["url"], method=creat_customer["method"],
                                data=creat_customer["data"],
                                headers=get_token)
        logger.info([creat_customer['title'], result])
        assert result['body']['msg'] == "成功" and creat_customer['data']['customerCode'] == \
               CommonDatabase().select_data(
                   "customer_code", "base_tm_customer", f"customer_code ='{creat_customer['data']['customerCode']}'")[
                   'customer_code']
        CommonDatabase().delete_data("base_tm_customer", f"customer_code ='{creat_customer['data']['customerCode']}'")

    @allure.title("新增供应商接口")
    @pytest.mark.parametrize("creat_supplier", base_create_supplier)  # 测试新增供应商数据
    def test_create_supplier(self, creat_supplier, get_token):
        result = Request().send(url=creat_supplier["url"], method=creat_supplier["method"],
                                data=creat_supplier["data"],
                                headers=get_token)
        logger.info([creat_supplier['title'], result])
        assert result['body']['msg'] == "成功" and creat_supplier['data'][
            'supplierCode'] == CommonDatabase().select_data("supplier_code", "base_tm_supplier",
                                                            f"supplier_code='{creat_supplier['data']['supplierCode']}'")[
                   'supplier_code']
        CommonDatabase().delete_data("base_tm_supplier", f"supplier_code='{creat_supplier['data']['supplierCode']}'")

    @allure.title("新增店铺接口")
    @pytest.mark.parametrize("creat_shop", base_create_shop)  # 测试新增店铺数据
    def test_create_shop(self, creat_shop, get_token):
        result = Request().send(url=creat_shop["url"], method=creat_shop["method"],
                                data=creat_shop["data"],
                                headers=get_token)
        logger.info([creat_shop['title'], result])
        assert result['body']['msg'] == "成功" and creat_shop['data'][
            'storeCode'] == CommonDatabase().select_data("store_code", "base_tm_store",
                                                         f"store_code='{creat_shop['data']['storeCode']}'")[
                   'store_code']
        CommonDatabase().delete_data("base_tm_store", f"store_code='{creat_shop['data']['storeCode']}'")

    @allure.title("新增生产企业接口")
    @pytest.mark.parametrize("creat_product_company", base_create_product_company)  # 测试新增生产企业数据
    def test_create_product_company(self, creat_product_company, get_token):
        result = Request().send(url=creat_product_company["url"], method=creat_product_company["method"],
                                data=creat_product_company["data"],
                                headers=get_token)
        logger.info([creat_product_company['title'], result])
        assert result['body']['msg'] == "成功" and creat_product_company['data'][
            'mfgCode'] == CommonDatabase().select_data("mfg_code", "base_tm_mfg",
                                                       f"mfg_code='{creat_product_company['data']['mfgCode']}'")[
                   'mfg_code']
        CommonDatabase().delete_data("base_tm_mfg", f"mfg_code='{creat_product_company['data']['mfgCode']}'")

    @allure.title("新增商品经营范围接口")
    @pytest.mark.parametrize("creat_commodity_range", base_create_commodity_range)  # 测试新增商品经营范围数据
    def test_create_commodity_range(self, creat_commodity_range, get_token):
        result = Request().send(url=creat_commodity_range["url"], method=creat_commodity_range["method"],
                                data=creat_commodity_range["data"],
                                headers=get_token)
        logger.info([creat_commodity_range['title'], result])
        assert result['body']['msg'] == "成功"

    @allure.title("删除商品经营范围接口")
    @pytest.mark.parametrize("delete_commodity_range", base_delete_commodity_range)  # 测试删除商品经营范围数据
    def test_delete_commodity_range(self, delete_commodity_range, get_token):
        commodity_range_id = CommonDatabase().select_data("id", "base_tm_sku_category",
                                                          f"category_code = '{read_yaml(Path.base_data_path, 'base_create_commodity_range')[0]['data']['categoryCode']}'")
        result = Request().send(url=delete_commodity_range["url"] + str(commodity_range_id['id']),
                                method=delete_commodity_range["method"],
                                data=delete_commodity_range["data"],
                                headers=get_token)
        logger.info([delete_commodity_range['title'], result])
        assert result['body']['msg'] == "成功"

    @allure.title("新增商品接口")
    @pytest.mark.parametrize("create_commodity", base_create_commodity)  # 测试新增商品数据
    def test_create_commodity(self, create_commodity, get_token):
        result = Request().send(url=create_commodity["url"],
                                method=create_commodity["method"],
                                data=create_commodity["data"],
                                headers=get_token)
        logger.info([create_commodity['title'], result])
        assert result['body']['msg'] == "成功" and create_commodity['data']['skuCode'] == \
               CommonDatabase().select_data("sku_code", "base_tm_sku",
                                            f"sku_code='{create_commodity['data']['skuCode']}'")[
                   'sku_code']

    @allure.title("删除商品数据接口")
    @pytest.mark.parametrize("delete_commodity", base_delete_commodity)  # 删除商品数据
    def test_delete_commodity(self, delete_commodity, get_token):
        sku_id = CommonDatabase().select_data("id", "base_tm_sku",
                                              f"sku_code = '{read_yaml(Path.base_data_path, 'base_create_commodity')[0]['data']['skuCode']}'")
        result = Request().send(url=delete_commodity["url"],
                                method=delete_commodity["method"],
                                data=[f'{sku_id["id"]}'],
                                headers=get_token)
        logger.info([delete_commodity['title'], result])
        assert result['body']['msg'] == "成功"

    @allure.title("商品详情查询接口")
    @pytest.mark.parametrize("commodity_details", base_commodity_details)  # 商品详情接口
    def test_commodity_details(self, commodity_details, get_token):
        result = Request().send(url=commodity_details["url"],
                                method=commodity_details["method"],
                                data=commodity_details['data'],
                                headers=get_token)
        logger.info([commodity_details['title'], result])
        assert result['body']['msg'] == "成功" and result['body']['obj'] != {}

    @allure.title("商品编辑接口")
    @pytest.mark.parametrize("commodity_update", base_update_details)  # 商品编辑接口
    def test_commodity_update(self, commodity_update, get_token):
        result = Request().send(url=commodity_update["url"],
                                method=commodity_update["method"],
                                data=commodity_update['data'],
                                headers=get_token)
        logger.info([commodity_update['title'], result])
        assert result['body']['msg'] == "成功" and result['body']['obj'] != {}

    @allure.title("商品监管查看接口")
    @pytest.mark.parametrize("commodity_supervise_details", base_commodity_supervise_details)  # 商品监管查看接口
    def test_commodity_supervise_details(self, commodity_supervise_details, get_token):
        result = Request().send(url=commodity_supervise_details["url"],
                                method=commodity_supervise_details["method"],
                                data=commodity_supervise_details['data'],
                                headers=get_token)
        logger.info([commodity_supervise_details['title'], result])
        assert result['body']['msg'] == "成功" and result['body']['obj'] != {}

    @allure.title("商品监管编辑接口")
    @pytest.mark.parametrize("commodity_supervise_update", base_commodity_supervise_update)  # 商品监管编辑接口
    def test_commodity_supervise_update(self, commodity_supervise_update, get_token):
        result = Request().send(url=commodity_supervise_update["url"],
                                method=commodity_supervise_update["method"],
                                data=commodity_supervise_update['data'],
                                headers=get_token)
        logger.info([commodity_supervise_update['title'], result])
        assert result['body']['msg'] == "成功" and result['body']['obj'] != {}

    @allure.title("仓储容器新增接口")
    @pytest.mark.parametrize("create_container", base_create_container)  # 仓储容器新增接口
    def test_create_container(self, create_container, get_token):
        result = Request().send(url=create_container["url"],
                                method=create_container["method"],
                                data=create_container['data'],
                                headers=get_token)
        logger.info([create_container['title'], result])
        assert result['body']['msg'] == "成功" and create_container['data']['containerBarcode'] == \
               CommonDatabase().select_data("container_barcode", "base_tm_container",
                                            f"container_barcode = '{create_container['data']['containerBarcode']}'")[
                   'container_barcode']

    @allure.title("仓储容器删除接口")
    @pytest.mark.parametrize("delete_container", base_delete_container)  # 仓储容器删除接口
    def test_delete_container(self, delete_container, get_token):
        container_id = CommonDatabase().select_data("id", "base_tm_container",
                                                    f"container_barcode = '{read_yaml(Path.base_data_path, 'base_create_container')[0]['data']['containerBarcode']}'")
        result = Request().send(url=delete_container["url"] + str(container_id["id"]),
                                method=delete_container["method"],
                                data=[f'{container_id["id"]},'],
                                headers=get_token)
        logger.info([delete_container['title'], result])
        assert result['body']['msg'] == "成功"

    @allure.title("滑道新增接口")
    @pytest.mark.parametrize("create_slide", base_create_slide)  # 滑道新增接口
    def test_create_slide(self, create_slide, get_token):
        result = Request().send(url=create_slide["url"],
                                method=create_slide["method"],
                                data=create_slide['data'],
                                headers=get_token)
        logger.info([create_slide['title'], result])
        assert result['body']['msg'] == "成功" and create_slide['data']['slidewayCode'] == \
               CommonDatabase().select_data("slideway_code", "base_tm_inner_review_sorting_slideway",
                                            f"slideway_code = '{create_slide['data']['slidewayCode']}'")[
                   'slideway_code']

    @allure.title("滑道删除接口")
    @pytest.mark.parametrize("delete_slide", base_delete_slide)  # 滑道删除接口
    def test_delete_slide(self, delete_slide, get_token):
        slide_id = CommonDatabase().select_data("id", "base_tm_inner_review_sorting_slideway",
                                                f"slideway_code = '{read_yaml(Path.base_data_path, 'base_create_slide')[0]['data']['slidewayCode']}'")
        result = Request().send(url=delete_slide["url"] + str(slide_id["id"]),
                                method=delete_slide["method"],
                                data=[f'{slide_id["id"]},'],
                                headers=get_token)
        logger.info([delete_slide['title'], result])
        assert result['body']['msg'] == "成功"

    @allure.title("件货台新增接口")
    @pytest.mark.parametrize("create_pick_container", base_create_pick_container)  # 拣货台新增接口
    def test_create_pick_container(self, create_pick_container, get_token):
        result = Request().send(url=create_pick_container["url"],
                                method=create_pick_container["method"],
                                data=create_pick_container['data'],
                                headers=get_token)
        logger.info([create_pick_container['title'], result])
        assert result['body']['msg'] == "成功" and create_pick_container['data']['pickDeskNo'] == \
               CommonDatabase().select_data("pick_desk_no", "base_tm_pick_desk",
                                            f"pick_desk_no = '{create_pick_container['data']['pickDeskNo']}'")[
                   'pick_desk_no']

    @allure.title("拣货台删除接口")
    @pytest.mark.parametrize("delete_pick_container", base_delete_pick_container)  # 件货台删除接口
    def test_delete_pick_container(self, delete_pick_container, get_token):
        pick_desk_id = CommonDatabase().select_data("id", "base_tm_pick_desk",
                                                    f"pick_desk_no = '{read_yaml(Path.base_data_path, 'base_create_pick_container')[0]['data']['pickDeskNo']}'")
        result = Request().send(url=delete_pick_container["url"] + str(pick_desk_id["id"]),
                                method=delete_pick_container["method"],
                                data=[f'{pick_desk_id["id"]},'],
                                headers=get_token)
        logger.info([delete_pick_container['title'], result])
        assert result['body']['msg'] == "成功"

    @allure.title("作业台新增接口")
    @pytest.mark.parametrize("create_work_container", base_create_work_container)  # 作业台新增接口
    def test_create_work_container(self, create_work_container, get_token):
        result = Request().send(url=create_work_container["url"],
                                method=create_work_container["method"],
                                data=create_work_container['data'],
                                headers=get_token)
        logger.info([create_work_container['title'], result])
        assert result['body']['msg'] == "成功" and create_work_container['data']['recheckDeskCode'] == \
               CommonDatabase().select_data("recheck_desk_code", "base_tm_recheck_desk",
                                            f"recheck_desk_code = '{create_work_container['data']['recheckDeskCode']}'")[
                   'recheck_desk_code']

    @allure.title("作业台删除接口")
    @pytest.mark.parametrize("delete_work_container", base_delete_work_container)  # 作业台删除接口
    def test_delete_work_container(self, delete_work_container, get_token):
        work_desk_id = CommonDatabase().select_data("id", "base_tm_recheck_desk",
                                                    f"recheck_desk_code = '{read_yaml(Path.base_data_path, 'base_create_work_container')[0]['data']['recheckDeskCode']}'")
        result = Request().send(url=delete_work_container["url"] + str(work_desk_id["id"]),
                                method=delete_work_container["method"],
                                data=[f'{work_desk_id["id"]},'],
                                headers=get_token)
        logger.info([delete_work_container['title'], result])
        assert result['body']['msg'] == "成功"

    @allure.title("托运公司档案新增接口")
    @pytest.mark.parametrize("create_consignment", base_create_consignment)  # 托运公司档案新增接口，暂时设置物理删除，先阶段无法通过接口删除
    def test_create_consignment(self, create_consignment, get_token):
        result = Request().send(url=create_consignment["url"],
                                method=create_consignment["method"],
                                data=create_consignment['data'],
                                headers=get_token)
        logger.info([create_consignment['title'], result])
        assert result['body']['msg'] == "成功" and create_consignment['data']['carrierCode'] == \
               CommonDatabase().select_data("carrier_code", "base_tm_carrier",
                                            f"carrier_code = '{create_consignment['data']['carrierCode']}'")[
                   'carrier_code']
        CommonDatabase().delete_data("base_tm_carrier", f"carrier_code = '{create_consignment['data']['carrierCode']}'")

    @allure.title("erp承运商新增接口")
    @pytest.mark.parametrize("create_erp_consignment", base_create_erp_consignment)  # erp承运商新增接口
    def test_create_erp_consignment(self, create_erp_consignment, get_token):
        result = Request().send(url=create_erp_consignment["url"],
                                method=create_erp_consignment["method"],
                                data=create_erp_consignment['data'],
                                headers=get_token)
        logger.info([create_erp_consignment['title'], result])
        assert result['body']['msg'] == "成功" and create_erp_consignment['data']['carrierCode'] == \
               CommonDatabase().select_data("carrier_code", "base_tm_erp_carrier",
                                            f"carrier_code = '{create_erp_consignment['data']['carrierCode']}'")[
                   'carrier_code']
        CommonDatabase().delete_data("base_tm_erp_carrier",
                                     f"carrier_code = '{create_erp_consignment['data']['carrierCode']}'")

    @allure.title("方向线路信息新增接口")
    @pytest.mark.parametrize("create_road_data", base_create_road_data)  # 方向线路信息新增接口
    def test_create_road_data(self, create_road_data, get_token):
        result = Request().send(url=create_road_data["url"],
                                method=create_road_data["method"],
                                data=create_road_data['data'],
                                headers=get_token)
        logger.info([create_road_data['title'], result])
        assert result['body']['msg'] == "成功" and create_road_data['data']['routeCode'] == \
               CommonDatabase().select_data("route_code", "base_tm_direction_route",
                                            f"route_code = '{create_road_data['data']['routeCode']}'")[
                   'route_code']

    @allure.title("方向线路信息删除接口")
    @pytest.mark.parametrize("delete_road", base_delete_road_data)  # 方向线路信息删除接口
    def test_delete_road(self, delete_road, get_token):
        road_id = CommonDatabase().select_data("id", "base_tm_direction_route",
                                               f"route_code = '{read_yaml(Path.base_data_path, 'base_create_road_data')[0]['data']['routeCode']}'")
        result = Request().send(url=delete_road["url"] + str(road_id["id"]),
                                method=delete_road["method"],
                                data=[f'{road_id["id"]},'],
                                headers=get_token)
        logger.info([delete_road['title'], result])
        assert result['body']['msg'] == "成功"

    @allure.title("发货信息新增接口")
    @pytest.mark.parametrize("create_consignment_data", base_create_consignment_data)  # 发货信息新增接口
    def test_create_consignment_data(self, create_consignment_data, get_token):
        result = Request().send(url=create_consignment_data["url"],
                                method=create_consignment_data["method"],
                                data=create_consignment_data['data'],
                                headers=get_token)
        logger.info([create_consignment_data['title'], result])
        assert result['body']['msg'] == "成功"

        # # @pytest.mark.parametrize("delete_consignment", base_delete_consignment_data)  # 发货信息删除接口
        # # def test_delete_consignment(self, delete_consignment, get_token):
        # #     road_id = CommonDatabase().select_data("id", "base_tm_driver",
        # #                                            f"driver_code = '{read_yaml(Path.base_data_path, 'base_create_consignment_data')[0]['data']['routeCode']}'")
        # #     result = Request().send(url=delete_consignment["url"] + str(road_id["id"]),
        # #                             method=delete_consignment["method"],
        # #                             data=[f'{road_id["id"]},'],
        # #                             headers=get_token)
        # #     logger.info([result])
        # assert result['body']['msg'] == "成功"

    @allure.title("司机信息新增接口")
    @pytest.mark.parametrize("creat_driver", base_create_driver_data)  # 司机信息新增接口
    def test_create_driver_data(self, creat_driver, get_token):
        result = Request().send(url=creat_driver["url"],
                                method=creat_driver["method"],
                                data=creat_driver['data'],
                                headers=get_token)
        logger.info([creat_driver['title'], result])
        assert result['body']['msg'] == "成功" and creat_driver['data']['driverCode'] == \
               CommonDatabase().select_data("driver_code", "base_tm_driver",
                                            f"driver_code = '{creat_driver['data']['driverCode']}'")[
                   'driver_code']

    @allure.title("司机信息删除接口")
    @pytest.mark.parametrize("delete_driver", base_delete_driver_data)  # 司机信息删除接口
    def test_delete_driver(self, delete_driver, get_token):
        road_id = CommonDatabase().select_data("id", "base_tm_driver",
                                               f"driver_code = '{read_yaml(Path.base_data_path, 'base_create_driver_data')[0]['data']['driverCode']}'")
        result = Request().send(url=delete_driver["url"] + str(road_id["id"]),
                                method=delete_driver["method"],
                                data=[f'{road_id["id"]},'],
                                headers=get_token)
        logger.info([delete_driver['title'], result])
        assert result['body']['msg'] == "成功"

    @allure.title("车辆信息新增接口")
    @pytest.mark.parametrize("creat_car", base_create_car_data)  # 车辆信息新增接口
    def test_create_car_data(self, creat_car, get_token):
        result = Request().send(url=creat_car["url"],
                                method=creat_car["method"],
                                data=creat_car['data'],
                                headers=get_token)
        logger.info([creat_car['title'], result])
        assert result['body']['msg'] == "成功" and creat_car['data']['mnemonicCode'] == \
               CommonDatabase().select_data("mnemonic_code", "base_tm_vehicle",
                                            f"mnemonic_code = '{creat_car['data']['mnemonicCode']}'")[
                   'mnemonic_code']

    @allure.title("车辆信息删除接口")
    @pytest.mark.parametrize("delete_car", base_delete_car_data)  # 车辆信息删除接口
    def test_delete_car(self, delete_car, get_token):
        road_id = CommonDatabase().select_data("id", "base_tm_vehicle",
                                               f"mnemonic_code = '{read_yaml(Path.base_data_path, 'base_create_car_data')[0]['data']['mnemonicCode']}'")
        result = Request().send(url=delete_car["url"] + str(road_id["id"]),
                                method=delete_car["method"],
                                data=[f'{road_id["id"]},'],
                                headers=get_token)
        logger.info([delete_car['title'], result])
        assert result['body']['msg'] == "成功"
