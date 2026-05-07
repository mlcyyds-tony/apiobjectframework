# -*- coding: UTF-8 -*-
# @Project ：apiobjectframework
# @File ：run.py
# @IDE ：PyCharm
# @Author ：小甜材
# @Date ：2023/7/20 20:20

import os
import sys

import pytest

from common.file_load import load_yaml_file, write_yaml
from paths_manager import common_yaml_path, http_yaml_path, db_yaml_path, redis_yaml_path

if __name__ == '__main__':
    args = sys.argv # 表示获取终端执行时传递的参数
    print(args) # args是个列表，第一个元素是run.py文件名，第二个元素是环境名称
    env_file = 'config/env_test.yml'
    if len(args)>1:
        env_name = args[1] #获取环境名称
        # 拼接环境文件路径
        env_file = f'config/env_{env_name}.yml'
        del args[1] # 删除传进来的环境名称参数，否则会被当做pytest要执行的测试用例名称
    # 读取要执行的环境的配置文件，获取所有配置信息
    env_info = load_yaml_file(env_file)
    # 依次写入到各个配置文件中去
    write_yaml(common_yaml_path,env_info['common'])
    write_yaml(http_yaml_path, env_info['http'])
    write_yaml(db_yaml_path, env_info['db'])
    write_yaml(redis_yaml_path, env_info['redis'])
    # pytest.main()自动扫描当前pytest.ini中相关的配置，根据配置执行测试
    pytest.main()

    # 这个是直接打开测试报告，仅仅用于本地自己看
    os.system('allure serve report/data')
