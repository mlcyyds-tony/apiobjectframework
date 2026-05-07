# encoding: utf-8 -*-*-
# @file     : base_api.py
# @author   : 小甜材
# @Time     : 2026/4/20 20:58




from common.client import RequestsClient

# 买家服务基类
from common.file_load import load_yaml_file
from paths_manager import http_yaml_path


class BaseBuyerApi(RequestsClient):
    # 这是定义的全局性的类属性，来代表买家token，默认是空
    # token提取赋值是在测试之前要完成的，最终会在自定义的fixture中完成
    buyer_token = ''
    uid = ''
    def __init__(self):
        super().__init__() # 表示继承父类所有的属性
        self.host = load_yaml_file(http_yaml_path)['buyer']
        self.headers = {
            "Authorization":BaseBuyerApi.buyer_token
        }

# 卖家服务基类
class BaseSellerApi(RequestsClient):
    # 这是定义的全局性的类属性，来代表买家token，默认是空
    # token提取赋值是在测试之前要完成的，最终会在自定义的fixture中完成
    seller_token = ''
    def __init__(self):
        super().__init__() # 表示继承父类所有的属性
        self.host = load_yaml_file(http_yaml_path)['seller']
        self.headers = {
            "Authorization":BaseSellerApi.seller_token
        }
# 管理员服务基类
class BaseManagerApi(RequestsClient):
    # 这是定义的全局性的类属性，来代表买家token，默认是空
    # token提取赋值是在测试之前要完成的，最终会在自定义的fixture中完成
    manager_token = ''
    def __init__(self):
        super().__init__() # 表示继承父类所有的属性
        self.host = load_yaml_file(http_yaml_path)['manager']
        self.headers = {
            "Authorization":BaseManagerApi.manager_token
        }

# 基础服务基类
class BaseBasicApi(RequestsClient):

    def __init__(self):
        super().__init__() # 表示继承父类所有的属性
        self.host = load_yaml_file(http_yaml_path)['basic']

