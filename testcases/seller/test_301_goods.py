# encoding: utf-8 -*-*-
# @file     : test_301_goods.py
# @author   : 小甜材
# @Time     : 2026/5/1 20:03

import allure
import pytest

from api.seller.goods_apis import AddGoodsApi
from common.file_load import load_yaml_file
from common.json_util import update_value_to_json
from paths_manager import mtxshop_data_yaml

@allure.epic('卖家接口测试')
@allure.feature('商品-商品相关接口')
@allure.story('添加商品接口测试')
class TestAddGoodsApi:

    test_data = load_yaml_file(mtxshop_data_yaml)['添加商品接口']
    @pytest.mark.parametrize('casename,new_params,expect_status,expect_body',test_data)
    def test_add_goods_exceptions(self,casename,new_params,expect_status,expect_body):
        allure.dynamic.title(casename)
        add_goods_api = AddGoodsApi()
        # 根据传入的new_params，调用update_value_to_json方法完成接口参数替换
        # new_params本身是一个字典，key是目标参数对应的json_path,value是目标参数对应的测试数据值
        for json_path,new_value in new_params.items():
            add_goods_api.json=update_value_to_json(add_goods_api.json,json_path,new_value)
        resp = add_goods_api.send()
        pytest.assume(resp.status_code == expect_status,f'期望值:{expect_status},实际值:{resp.status_code}')
        pytest.assume(resp.text == expect_body, f'期望值:{expect_body},实际值:{resp.text}')

    # # 商品名称为空
    # def test_add_goods_exceptions1(self):
    #     add_goods_api = AddGoodsApi()
    #     # 将接口参数 商品名称 写成空字符串
    #     add_goods_api.json['goods_name'] = ''
    #     resp = add_goods_api.send()
    #     pytest.assume(resp.status_code == 400,f'期望值:400,实际值:{resp.status_code}')
    #     pytest.assume(resp.text == '{"code":"004","message":"商品名称不能为空"}', f'期望值:{{"code":"004","message":"商品名称不能为空"}},实际值:{resp.text}')
    # # 商品编号为空
    # def test_add_goods_exceptions2(self):
    #     add_goods_api = AddGoodsApi()
    #     # 将接口参数 商品名称 写成空字符串
    #     add_goods_api.json['sn'] = ''
    #     resp = add_goods_api.send()
    #     pytest.assume(resp.status_code == 400,f'期望值:400,实际值:{resp.status_code}')
    #     pytest.assume(resp.text == '{"code":"004","message":"商城编号不能为空"}', f'期望值:{{"code":"004","message":"商城编号不能为空"}},实际值:{resp.text}')

