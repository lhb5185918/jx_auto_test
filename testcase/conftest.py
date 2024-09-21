import pytest
import requests
from utils.getyamldata import *
from config.path import Path
import random
import json


@pytest.fixture(scope='session')
def get_token():
    url = read_yaml(Path.config_file_path, 'login_data', 'url')
    data = {"userNo": "lhb001",
            "pwd": "lhx7758521",
            "platForm": "app",
            "companyCode": "ZHQC",
            "whId": 1,
            "warehouseId": "",
            "haveWarehouse": 1,
            "clientId": "iowtb-new",
            "userLanguage": "zh-CN"}
    res = requests.post(url=url, json=data, headers={'Content-Type': 'application/json'})
    token = res.json()['obj']['token']
    headers = {'Content-Type': 'application/json', 'Authorization': token}
    return headers
