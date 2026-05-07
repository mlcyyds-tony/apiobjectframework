# encoding: utf-8 -*-*-
# @file     : test_002_create_trade.py
# @author   : 小甜材
# @Time     : 2026/4/22 15:24

import allure
import pytest

from api.buyer.cart_apis import BuyNowApi, DeleteCartApi, AddCartApi
from api.buyer.create_trade_apis import CreateTradeApi
from common.file_load import load_yaml_file
from paths_manager import mtxshop_data_yaml

@allure.epic('买家接口测试')
@allure.feature('交易接口模块')
@allure.story('创建交易接口测试')
class TestCreateTradeApi:


    # client_data = ['PC','WAP','NATIVE','REACT','MINI']
    # way_data = ['BUY_NOW','CART']
    datas = load_yaml_file(mtxshop_data_yaml)['创建交易接口']
    client_data = datas['client']
    way_data = datas['way']

    @pytest.mark.parametrize('client', client_data)  # 5个数据
    @pytest.mark.parametrize('way', way_data)  # 2个数据
    def test_create_trade(self, client, way):  # 生成数据总数5*2=10
        allure.dynamic.title(f'{client}-{way}')
        # buyer_login()
        # 如果way是BUY_NOW就调用立即购买接口
        # 如果是CART就调用添加购物车接口
        if way == 'BUY_NOW':
            BuyNowApi(sku_id=541).send()
        elif way == 'CART':
            # 先清空购物车
            DeleteCartApi().send()
            AddCartApi(sku_id=541).send()
        resp = CreateTradeApi(client=client, way=way).send()
        print(resp.text)
        assert resp.status_code == 200
