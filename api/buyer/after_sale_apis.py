# encoding: utf-8 -*-*-
# @file     : after_sale_apis.py
# @author   : 小甜材
# @Time     : 2026/4/25 20:34



from api.base_api import BaseBuyerApi


class ReturnGoodsApi(BaseBuyerApi):

    def __init__(self,order_sn,sku_id,region=2799):
        super().__init__()
        self.url = f'{self.host}/after-sales/apply/return/goods'
        self.method = 'post'
        self.data = {
            "service_type": "RETURN_GOODS",
            "return_num": 1,
            "ship_addr": "北京霍营",
            "ship_name": "材哥20260327",
            "ship_mobile": "18729399607",
            "account_type": "BANKTRANSFER",
            "bank_name": "银行名称",
            "bank_deposit_name": "北京开户行",
            "bank_account_name": "材哥",
            "bank_account_number": "43423423434434",
            "reason": "不想要了",
            "problem_desc": "没啥描述就是不想要了",
            "order_sn": order_sn,
            "sku_id": sku_id,
            "apply_vouchers":"",
            "region": region #2799
        }