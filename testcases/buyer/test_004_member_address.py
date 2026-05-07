# encoding: utf-8 -*-
# @file     : test_004_member_address.py
# @author   : 小甜材
# @Time     : 2026/5/1 21:20

import allure
import pytest

from api.buyer.member_address_apis import AddAddressApi
from common.file_load import load_yaml_file
from common.json_util import update_value_to_json
from paths_manager import mtxshop_data_yaml

@allure.epic('买家接口测试')
@allure.feature('会员-会员地址接口模块')
@allure.story('添加收货地址接口测试')
class TestAddAddressApi:

    test_data = load_yaml_file(mtxshop_data_yaml)['添加收货地址接口']
    @pytest.mark.parametrize('casename,new_params,expect_status,expect_body',test_data)
    def test_add_address_exceptions(self,casename,new_params,expect_status,expect_body):
        allure.dynamic.title(casename)
        add_address_api = AddAddressApi()
        # 根据传入的new_params，调用update_value_to_json方法完成接口参数替换
        # new_params本身是一个字典，key是目标参数对应的json_path,value是目标参数对应的测试数据值
        for json_path,new_value in new_params.items():
            add_address_api.data=update_value_to_json(add_address_api.data,json_path,new_value)
        resp = add_address_api.send()
        pytest.assume(resp.status_code == expect_status,f'期望值:{expect_status},实际值:{resp.status_code}')
        pytest.assume(resp.text == expect_body, f'期望值:{expect_body},实际值:{resp.text}')