# encoding: utf-8 -*-*-
# @file     : order_apis.py
# @author   : 小甜材
# @Time     : 2026/4/25 20:21

from api.base_api import BaseSellerApi


class OrderDeliveryApi(BaseSellerApi):

    def __init__(self,order_sn):
        super().__init__()
        self.url = f'{self.host}/seller/trade/orders/{order_sn}/delivery'
        self.method = 'post'
        self.data = {
            "ship_no":"ashhdhdh",# 快递号
            "logi_id":13,
            "logi_name":"中通01"
        }

class OrderPayApi(BaseSellerApi):

    def __init__(self,order_sn,pay_price):
        super().__init__()
        self.url = f'{self.host}/seller/trade/orders/{order_sn}/pay'
        self.method = 'post'
        self.data = {
            "pay_price":pay_price
        }