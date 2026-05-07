# encoding: utf-8 -*-
# @file     : test_900_order_flow.py
# @author   : 小甜材
# @Time     : 2026/4/25 21:02

import time

import allure
import javaobj
import jsonpath
import pytest

from api.base_api import BaseBuyerApi
from api.buyer.after_sale_apis import ReturnGoodsApi
from api.buyer.cart_apis import BuyNowApi, AddCartApi, DeleteCartApi
from api.buyer.comment_apis import AddCommentApi
from api.buyer.create_trade_apis import CreateTradeApi
from api.buyer.order_apis import OrderRogApi
from api.seller.order_apis import OrderDeliveryApi, OrderPayApi
from common.file_load import load_yaml_file
from common.json_util import extract_json
from paths_manager import mtxshop_data_yaml

@allure.epic('主流程测试')
@allure.feature('订单流程测试')
class TestOrderFlow:
    # 将order_sn作为类属性定义和赋值，可以用来作为当前流程中的关联数据
    order_sn = ''
    pay_price = 0

    @allure.title('立即购买')
    def test_buy_now(self,redis_init,goods_data,init_order_params):
        # goods_data 会得到(goods_id,sku_id)
        resp = BuyNowApi(sku_id=goods_data[1]).send()
        assert resp.status_code == 200
        res = redis_init.get(f'{{BUY_NOW_ORIGIN_DATA_PREFIX}}_{BaseBuyerApi.uid}')
        res_object = javaobj.loads(res)
        buy_now_object = res_object[0]
        skuId=buy_now_object.__getattribute__('skuId')
        num = buy_now_object.__getattribute__('num')
        pytest.assume(skuId == goods_data[1], f'期望值:{goods_data[1]},实际值:{skuId}')
        pytest.assume(num == 1, f'期望值:1,实际值:{num}')

    @allure.title('立即购买的创建交易')
    def test_create_trade_buynow(self):
        resp = CreateTradeApi().send()
        assert resp.status_code == 200

    @allure.title('添加购物车')
    def test_add_cart(self,goods_data):
        resp = AddCartApi(sku_id=goods_data[1]).send()
        assert resp.status_code == 200

    @allure.title('添加购物车的创建交易')
    def test_create_trade_addcart(self,db_init):
        resp = CreateTradeApi(way='CART').send()
        assert resp.status_code == 200
        # 从创建交易的接口中提取响应中的订单号
        # 使用json提取数据
        # TestOrderFlow.order_sn = jsonpath.jsonpath(resp.json(),'$..sn')[0]
        TestOrderFlow.order_sn = extract_json(resp.json(),'$..sn')
        # TestOrderFlow.pay_price = jsonpath.jsonpath(resp.json(),'$..total_price')[0]
        TestOrderFlow.pay_price = extract_json(resp.json(), '$..total_price')
        # 数据库断言
        db_res = db_init.select(f"select *  FROM mtxshop_trade.es_order WHERE member_id={BaseBuyerApi.uid} and sn={TestOrderFlow.order_sn}")
        assert len(db_res) == 1

    @allure.title('卖家发货')
    def test_order_delivery(self,db_init):
        time.sleep(2)
        # 该接口需要订单号，订单号从何而来
        resp = OrderDeliveryApi(order_sn=TestOrderFlow.order_sn).send()
        assert resp.status_code == 200
        # 数据库断言
        db_res = db_init.select(f"select order_status FROM mtxshop_trade.es_order WHERE member_id={BaseBuyerApi.uid} and sn={TestOrderFlow.order_sn}")
        db_order_status = db_res[0]['order_status']
        pytest.assume(db_order_status == "SHIPPED", f'期望值:SHIPPED,实际值:{db_order_status}')

    @allure.title('买家收货')
    def test_order_rog(self,db_init):
        time.sleep(2)
        resp = OrderRogApi(order_sn=TestOrderFlow.order_sn).send()
        assert resp.status_code == 200
        # 数据库断言
        db_res = db_init.select(f"select order_status FROM mtxshop_trade.es_order WHERE member_id={BaseBuyerApi.uid} and sn={TestOrderFlow.order_sn}")
        db_order_status = db_res[0]['order_status']
        pytest.assume(db_order_status == "ROG", f'期望值:ROG,实际值:{db_order_status}')

    @allure.title('卖家收款')
    def test_seller_pay(self,db_init):
        time.sleep(2)
        resp = OrderPayApi(order_sn=TestOrderFlow.order_sn,pay_price=TestOrderFlow.pay_price).send()
        assert resp.status_code == 200
        # 数据库断言
        db_res = db_init.select(f"select order_status FROM mtxshop_trade.es_order WHERE member_id={BaseBuyerApi.uid} and sn={TestOrderFlow.order_sn}")
        db_order_status = db_res[0]['order_status']
        pytest.assume(db_order_status == "PAID_OFF", f'期望值:PAID_OFF,实际值:{db_order_status}')

    @allure.title('买家评论')
    def test_comment(self,goods_data):
        time.sleep(2)
        resp = AddCommentApi(order_sn=TestOrderFlow.order_sn,sku_id=goods_data[1]).send()
        assert resp.status_code == 200

    @allure.title('买家申请退货')
    @pytest.mark.flaky(reruns=2,reruns_delay=10)
    def test_return_goods(self,goods_data):
        time.sleep(2)
        resp = ReturnGoodsApi(order_sn=TestOrderFlow.order_sn,sku_id=goods_data[1]).send()
        assert resp.status_code == 200


