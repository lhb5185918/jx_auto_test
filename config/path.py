import os


class Path:
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    common_path = project_path + os.sep + "common"

    config_path = project_path + os.sep + "config"

    log_path = project_path + os.sep + "log"

    report_path = project_path + os.sep + "report"

    setting_path = project_path + os.path.sep + "setting"

    config_file_path = project_path + os.path.sep + "testdata" + os.path.sep + "config.yaml"

    base_data_path = project_path + os.path.sep + "testdata" + os.path.sep + "base_data.yaml"

    in_order_path = project_path + os.path.sep + "testdata" + os.path.sep + "in_order.yaml"

    middle_data_path = project_path + os.path.sep + "testdata" + os.path.sep + "middle_data.yaml"

    data_path = project_path + os.path.sep + "testdata"

    util_path = project_path + os.path.sep + "utils"

    picture_path = project_path + os.path.sep + "testdata" + os.path.sep + "tp1.png"

    inside_middle_data_path = project_path + os.path.sep + "testdata" + os.path.sep + "inside_middle_data.yaml"

    warehouse_inside_path = project_path + os.path.sep + "testdata" + os.path.sep + "warehouse_inside_data.yaml"

    test_result_data = project_path + os.path.sep + "testdata" + os.path.sep + "test_result_data.yaml"

    gsp_management_path = project_path + os.path.sep + "testdata" + os.path.sep + "gsp_management_data.yaml"

    gsp_middle_data_path = project_path + os.path.sep + "testdata" + os.path.sep + "gsp_middle_data.yaml"

    out_order_data_path = project_path + os.path.sep + "testdata" + os.path.sep + "out_order_data.yaml"

    out_order_middle_path = project_path + os.path.sep + "testdata" + os.path.sep + "out_order_middle.yaml"

    delivery_management_path = project_path + os.path.sep + "testdata" + os.path.sep + "delivery_management_data.yaml"

    delivery_middle_path = project_path + os.path.sep + "testdata" + os.path.sep + "delivery_middle_data.yaml"

    report_forms_path = project_path + os.path.sep + "testdata" + os.path.sep + "warehouse_report_forms.yaml"

    special_data_path = project_path + os.path.sep + "testdata" + os.path.sep + "special_data.yaml"

    special_middle_path = project_path + os.path.sep + "testdata" + os.path.sep + "special_middle_data.yaml"

