import pytest
from config.path import *
from utils.getyamldata import *
from utils.requests_util import Request
from utils.log import logger
from utils.mysql_util import CommonDatabase


class TestBaseData:
    in_order_select_data = read_yaml(Path.in_order_path, "in_order_select_data")

    @pytest.mark.parametrize("in_order_data", in_order_select_data)  # 获取仓库列表接口
    def test_in_order_data(self, in_order_data, get_token):
        result = Request().send(url=in_order_data["url"], method=in_order_data["method"], data=in_order_data["data"],
                                headers=get_token)
        logger.info(result)
        assert result['code'] == 200 and result["body"] is not None


