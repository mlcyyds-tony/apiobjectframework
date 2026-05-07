# encoding: utf-8 -*-*-
# @file     : db_util.py
# @author   : 小甜材
# @Time     : 2026/4/18 20:57

import pymysql


class DBUtil:

    def __init__(self,host,user,password,port=3306):
        self.connect = pymysql.Connect(
            host=host,
            user=user,
            password=password,
            port=port,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        self.connect.commit() # 提交事务，如果不提交，那么下次查询，查不到最新的数据
        cursor.close()
        return data

    def update(self,sql):
        """
        insert、update、delete
        :param sql:
        :return:
        """
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()
    def close(self):
        if self.connect!=None:
            self.connect.close()

if __name__ == '__main__':
    db_util = DBUtil(host='59.36.173.55',user='mtxshop_test',password='mtxshamo')
    res = db_util.select('select *  FROM mtxshop_trade.es_order ORDER BY order_id DESC LIMIT 2')
    print(res[0]['order_status'])
    db_util.close()