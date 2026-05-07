# encoding: utf-8 -*-*-
# @file     : test_001_buy_now.py
# @author   : 小甜材
# @Time     : 2026/4/20 21:29

import allure
import pytest

from api.buyer.cart_apis import BuyNowApi
from common.file_load import read_excel
from paths_manager import mtxshop_data_xlsx

@allure.epic('买家接口测试')
@allure.feature('交易-购物车接口模块')
@allure.story('立即购买接口测试')
class TestBuyNowApi:

    # test_data = [
    #     ['产品id不存在',7273737,   1,   500,  '{"code":"004","message":"不合法"}'],
    #     ['num为0',     541,      0,    400, '{"code":"004","message":"购买数量必须大于0"}'],
    #     ['num为负数',   541,      -1,   400, '{"code":"004","message":"购买数量必须大于0"}'],
    #     ['num超过库存', 541, 99999999,   500, '{"code":"451","message":"商品库存已不足，不能购买。"}']
    # ]
    test_data = read_excel(mtxshop_data_xlsx, '立即购买测试数据')

    # @pytest.mark.repeat(2)
    # @allure.title('{casename}')
    @pytest.mark.parametrize('casename,sku_id,num,expect_status,expect_body',test_data)
    def test_buy_now(self,casename,sku_id,num,expect_status,expect_body):
        allure.dynamic.title(casename)
        # 实例化一个立即购买类的对象
        buy_now_api = BuyNowApi(sku_id=sku_id)
        # 由于BuyNowApi的init中并没有传递num，因此我们按照下面的方式把测试数据num传给该接口对象的参数
        buy_now_api.data['num'] = num
        # 接口对象已经准备好，发起接口调用
        resp = buy_now_api.send()
        print(resp.text)
        pytest.assume(resp.status_code == expect_status,f'期望值:{expect_status},实际值:{resp.status_code}')
        pytest.assume(resp.text == expect_body,f'期望值:{expect_body},实际值:{resp.text}')
