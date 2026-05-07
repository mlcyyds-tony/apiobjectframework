# encoding: utf-8 -*-*-
# @file     : login_apis.py
# @author   : 小甜材
# @Time     : 2026/4/25 20:04

from api.base_api import BaseSellerApi
from common.encry_decry import md5


class SellerLoginApi(BaseSellerApi):

    # 接口的基本信息，统一封装在init函数中
    def __init__(self,username,password):
        super().__init__()
        self.url = f'{self.host}/seller/login'
        self.method = 'get'
        self.params = {
            "username":username,
            "password":md5(password),
            "captcha":'1512',
            "uuid":"asdasdasdasdasdd"
        }