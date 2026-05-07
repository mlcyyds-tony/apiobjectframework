# -*- coding: UTF-8 -*-
# @Project ：apiobjectframework
# @File ：run.py
# @IDE ：PyCharm
# @Author ：小甜材
# @Date ：2026/4/22 15:03


import os
# 获取当前文件所在目录，其实就是项目根目录
project_path = os.path.dirname(__file__)
mtxshop_data_xlsx = f'{project_path}/data/mtxshop_data.xlsx'
mtxshop_data_yaml = f'{project_path}/data/mtxshop_data.yml'
common_yaml_path = f'{project_path}/config/common.yml'
http_yaml_path = f'{project_path}/config/http.yml'
redis_yaml_path = f'{project_path}/config/redis.yml'
db_yaml_path = f'{project_path}/config/db.yml'