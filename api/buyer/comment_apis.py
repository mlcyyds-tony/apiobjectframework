# encoding: utf-8 -*-*-
# @file     : comment_apis.py
# @author   : 小甜材
# @Time     : 2026/4/25 20:55



from api.base_api import BaseBuyerApi


class AddCommentApi(BaseBuyerApi):

    def __init__(self,order_sn,sku_id):
        super().__init__()
        self.url = f'{self.host}/members/comments'
        self.method = 'post'
        self.json = {
            "order_sn": order_sn,
            "delivery_score": 5,
            "description_score": 5,
            "service_score": 5,
            "comments": [{
                "sku_id": sku_id,
                "content": "这是评论内容不要在意",
                "grade": "good",
                "images": []
            }]
        }