# encoding: utf-8 -*-*-
# @file     : test_003_add_cart.py
# @author   : 小甜材
# @Time     : 2026/4/22 16:07

import allure
import pytest

from api.buyer.cart_apis import AddCartApi
from common.file_load import load_yaml_file
from paths_manager import mtxshop_data_yaml

@allure.epic('买家接口测试')
@allure.feature('交易-购物车接口模块')
@allure.story('添加购物车接口测试')
class TestAddCartApi:

    # test_data = [
    #     ['产品id不存在',7273737,   1,   500,  '{"code":"451","message":"商品已失效，请刷新购物车"}'],
    #     ['num为0',     541,      0,    400, '{"code":"004","message":"加入购物车数量必须大于0"}'],
    #     ['num为负数',   541,      -1,   400, '{"code":"004","message":"加入购物车数量必须大于0"}'],
    #     ['num超过库存', 541, 99999999,   500, '{"code":"451","message":"商品库存已不足，不能购买。"}']
    # ]
    test_data = load_yaml_file(mtxshop_data_yaml)['添加购物车接口']


    @pytest.mark.parametrize('casename,sku_id,num,expect_status,expect_body',test_data)
    def test_add_cart(self,casename,sku_id,num,expect_status,expect_body):
        allure.dynamic.title(casename)
        # 实例化一个立即购买类的对象
        add_cart_api = AddCartApi(sku_id=sku_id)
        # 由于BuyNowApi的init中并没有传递num，因此我们按照下面的方式把测试数据num传给该接口对象的参数
        add_cart_api.data['num'] = num
        # 接口对象已经准备好，发起接口调用
        resp = add_cart_api.send()
        print(resp.text)
        pytest.assume(resp.status_code == expect_status,f'期望值:{expect_status},实际值:{resp.status_code}')
        pytest.assume(resp.text == expect_body,f'期望值:{expect_body},实际值:{resp.text}')