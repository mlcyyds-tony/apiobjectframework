# encoding: utf-8 -*-*-
# @file     : login_apis.py
# @author   : 小甜材
# @Time     : 2026/4/20 21:08

from api.base_api import BaseBuyerApi
from common.encry_decry import md5


class BuyerLoginApi(BaseBuyerApi):

    # 接口的基本信息，统一封装在init函数中
    def __init__(self,username,password):
        super().__init__()
        self.url = f'{self.host}/passport/login'
        self.method = 'post'
        self.data = {
            "username":username,
            "password":md5(password),
            "captcha":'1512',
            "uuid":"asdasdasdasdasdd"
        }