                                 # encoding: utf-8 -*-*-                            
# @author: 材哥 微信：Matongxue_2
# @Time: 2021-12-20 9:29
# @Copyright：北京码同学

import time

from faker import Faker

fake = Faker(locale='zh_CN')


def rdm_phone_number():
    return fake.phone_number()

def cur_timestamp(level = 's'):#到毫秒级的时间戳
    if level=='s':
        return  int(time.time()) # 10位时间戳，精确到秒
    elif level == 'ms':
        return int(time.time() * 1000) # 13位时间戳，精确到毫秒
    else:
        raise Exception(f'{level}不支持')

def gen_timestamp(start_date='+0d',end_date='+1d'):
    date_time = fake.date_time_between(start_date=start_date,end_date=end_date)
    print(date_time)
    return int(time.mktime(date_time.timetuple()))

def cur_date():# 2022-09-29
    return fake.date_between_dates()

def cur_date_time():# 2022-09-29 10:07:33
    return fake.date_time_between_dates()

def rdm_date(pattern='%Y-%m-%d'):
    return fake.date(pattern=pattern)

def rdm_date_time():
    return fake.date_time()

if __name__ == '__main__':
    print(rdm_phone_number())
    print(rdm_date())
    print(rdm_date_time())
    print(cur_date())
    print(cur_timestamp())
    print(cur_date_time())
    # print(time.time())
    # print(time.time()*1000)
    print(gen_timestamp(start_date="-10d", end_date='+7d')) #day
    print(gen_timestamp(start_date="+0d", end_date='+7d'))
    print(gen_timestamp('-7d','-6d'))
