#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: sort_kdj.py

from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, wait

pool = ThreadPoolExecutor(max_workers=20)

############PROXY###########
timeout = 3

from tools import *

###多线程筛选
def sort_list(l, day=1):
    start_time = datetime.now()
    a = len(l)
    l1 = sort_kdj_list(l, day)
    b = len(l1)
    end_time = datetime.now()
    timedelsta = (end_time - start_time).seconds
    print('过滤掉%s支股票，还剩%s支股票，耗时%s秒。' % (a-b, b, timedelsta))
    return(l1)

########################### 筛选KDJ #############################

def sort_kdj(share_code, day=1):
    #print('检查 %s K是否低于J' % (share_code, target_price))
    kdj = kdj_now(share_code, day+1)
    if kdj == []:
        li.remove(share_code)
        print('%s 无法获取kdj。' % share_code)
    else:
        for i in kdj:
            if i[0] > kdj[1]:
                li.remove(share_code)
                print('%s 不符合条件。' % share_code)
                brake
            else:
                pass
        #print('%s 符合条件!' % share_code)


# 多线程筛选KDJ
def sort_kdj_list(l, day=1):
    global li
    print('筛选KDJ中, 一共%s支股票。' % len(l))
    li = list(l)
    futures = []
    for i in l:
        futures.append(pool.submit(sort_price, (i, day)))
    wait(futures)
    a = len(l)
    b = len(li)
    print('移除 %s 支股票J低于K，列表中还剩 %s' % (a-b, target_price, b))
    return(li)




def help():
    print('''
    多线程
    sort_list(list, price=18, day=10)
        sort_price_list(list, target_price=18)
          sort_price()
    help()
    ''')
