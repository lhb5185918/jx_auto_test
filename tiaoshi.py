from config.path import *
from utils.get_yaml_data import *
from utils.requests_util import Request
from utils.log import logger
from utils.other_utils import *
from utils.mysql_util import CommonDatabase

# rk_order_data:
# - order_id:
#     CGDD_order_id: 1
#     ZPCGDD_order_id: 1
#     TCSQD_order_id: 1
#     WDTKSQD_order_id: 1
#     PFXSTHD_order_id: 1
#     CGDDZP_order_id: 1
#     TCSQDZP_order_id: 1
#     DBRKD_order_id: 1
#     DBTCD_order_id: 1
#     LYTHD_order_id: 1
#     YCRKD_order_id: 1
#   order_no:
#     CGDD_order_no: 1
#     ZPCGDD_order_no: 1
#     TCSQD_order_no: 1
#     WDTKSQD_order_no: 1
#     PFXSTHD_order_no: 1
#     CGDDZP_order_no: 1
#     TCSQDZP_order_no: 1
#     DBRKD_order_no: 1
#     DBTCD_order_no: 1
#     LYTHD_order_no: 1
#     YCRKD_order_no: 1
#

from utils.mysql_util import CommonDatabase

# res = CommonDatabase().select_data("order_type",
#                                    "order_tt_in_order",
#                                    "id = 1931410042638848")[
#           "order_type"] + "_order_data"
# print(res)
# print(read_yaml(Path().middle_data_path, "rk_order_data", "order_data")[CommonDatabase().select_data("order_type",
#                                                                                                      "order_tt_in_order",
#                                                                                                      "id = 1931410042638848")[
# #                                                                             "order_type"] + "_order_data"])
#
# order_id = read_yaml(Path.middle_data_path, 'rk_order_data', "order_id")
# print(order_id)
# for order_id_data in [order_id[i] for i in order_id]:
#     print(order_id_data)
#     asn_new_data = read_yaml(Path().middle_data_path, "rk_order_data", "order_data")[
#                         CommonDatabase().select_data("order_type",
#                                                      "order_tt_in_order",
#                                                      f"id = '{order_id_data}'")[
#                             "order_type"] + "_order_data"
#                         ]
#     print(asn_new_data)


for i in read_yaml(Path().middle_data_path, "rk_order_data", "put_shelf_id"):
    if "CGDDZP" in i or "TCSQDZP" in i:
        print(i)