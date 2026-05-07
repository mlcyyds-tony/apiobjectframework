# encoding: utf-8 -*-*-
# @file     : goods_apis.py
# @author   : 小甜材
# @Time     : 2026/4/27 20:27

from api.base_api import BaseManagerApi


class GoodsBatchAuditApi(BaseManagerApi):

    def __init__(self,goods_ids:list):
        super().__init__()
        self.url = f'{self.host}/admin/goods/batch/audit'
        self.method = 'post'
        self.json = {
            "goods_ids": goods_ids,
            "message": "dsddd",
            "pass": 1
        }