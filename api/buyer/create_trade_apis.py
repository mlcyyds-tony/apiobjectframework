# encoding: utf-8 -*-*-
# @file     : create_trade_apis.py
# @author   : 小甜材
# @Time     : 2026/4/22 15:25

from api.base_api import BaseBuyerApi


class CreateTradeApi(BaseBuyerApi):

    def __init__(self,client='PC',way='BUY_NOW'):
        super().__init__()
        self.url = f'{self.host}/trade/create'
        self.method = 'post'
        self.data = {
            "client":client,
            "way":way
        }