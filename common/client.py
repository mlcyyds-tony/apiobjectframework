# encoding: utf-8 -*-*-
# @file     : client.py
# @author   : 小甜材
# @Time     : 2026/4/20 20:34

import requests

from common.encry_decry import AesEncryptECB
from common.logger import GetLogger


class RequestsClient:

    session = requests.session()

    # 要发起一个接口的调用需要用到哪些信息
    def __init__(self):
        self.url = None
        self.method = None
        self.headers = None
        self.params = None
        self.data = None
        self.json = None
        self.files = None
        self.resp = None
        # self.aes =AesEncryptECB(key='1234567890123456')

    def send(self):
        # 发起之前记录请求信息
        GetLogger.get_logger().debug(f'=================================================')
        GetLogger.get_logger().debug(f'接口url:{self.url}')
        GetLogger.get_logger().debug(f'接口method:{self.method}')
        GetLogger.get_logger().debug(f'接口headers:{self.headers}')
        GetLogger.get_logger().debug(f'接口params:{self.params}')
        GetLogger.get_logger().debug(f'接口data:{self.data}')
        GetLogger.get_logger().debug(f'接口json:{self.json}')
        GetLogger.get_logger().debug(f'接口files:{self.files}')

        # 如果说要统一完成加密，可以在这里完成
        # self.json = self.aes.encrypt(self.json)
        # verify=False 该参数表示忽略https的证书校验
        try:
            self.resp = RequestsClient.session.request(method=self.method,
                                                       url=self.url,
                                                       headers=self.headers,
                                                       params=self.params,
                                                       data=self.data,
                                                       json=self.json,
                                                       files=self.files,
                                                       verify=False)
            GetLogger.get_logger().debug(f'接口响应状态码:{self.resp.status_code}')
            GetLogger.get_logger().debug(f'接口响应body:{self.resp.text}')
        except BaseException as e:
            GetLogger.get_logger().exception(f'接口发起失败')
            raise BaseException(f'接口发起失败:{e}')

        return self.resp

    # def decry_body(self):
    #     return self.aes.decrypt(self.resp.text)
