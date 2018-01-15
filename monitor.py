#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: monitor.py

client_phone = 8618662059088

import sms
from tools import *
from datetime import datetime
from pytz import timezone
import threading
import os
import sqlite3

client_phone = 8615665156520
##########################################
# 监视程序
# 启动关闭MA监视
def start(l, debug=0):
    a = threading.Thread(target=kdj_monitor, args=(l, debug,))
    a.start()

def stop():
    globals()['monitor_status'] = False


# MA监视循环
def kdj_monitor(l, debug=0):
    global buy_list
    global monitor_status
    globals()['monitor_status'] = True
    buy_list = []
    create_ma_form('KDJ')
    text = '条件：1.前一日K小于D。 筛选出%s支股票，开始扫描。' % len(l)
    print('开始扫描。')
    #sms.send_sms(client_phone, text)
    sms.send_sms(16267318573, text)
    start_time = datetime.now(timezone('Asia/Shanghai'))
    dead_time = start_time.replace(hour=15, minute=00)
    if debug == 1:
        dead_time = start_time.replace(hour=23, minute=59)
    c = 0
    while datetime.now(timezone('Asia/Shanghai')) < dead_time:
        if globals()['monitor_status'] != False:
            c += 1
            # time.sleep(10)
            for i in l:
                kdj_checker(i)
            end_time = datetime.now(timezone('Asia/Shanghai'))
            timedelsta = (end_time - start_time).seconds
            print('第%s次扫描完成, 一共%s支股票，已找到%s支股票符合。 本次扫描耗时%s秒。' % (c, len(l), len(buy_list), timedelsta))
            start_time = end_time
        else:
            break
    print('监视结束！')


# KDJ监视条件
def kdj_checker(code):
    kdj = kdj_now(code)[0]
    #print(code)
    # K大于D
    if kdj[0] >= kdj[1]:
        if code not in buy_list:
            buy_list.append(code)
            time_now = datetime.now(timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
            text = '%s%s(KDJ)交叉提醒 %s' % (share_name(code), code, time_now)
            #sms.send_sms(client_phone, text)
            sms.send_sms(16267318573, text)
            print('%s买入时机' % code)
            insert_ma_data(code, kdj)


# 数据库部分
# 在数据库'KDJ'中建立表 '17-12-27'/ CODE/ NAME/ PRICE/ AVERAGE/ K/ D/ J/ TIME/ TIMECROSS/ MARKET
def create_ma_form(dbname):
    if os.path.exists('database') == False:
        os.makedirs('database')
    date = datetime.now(timezone('Asia/Shanghai')).strftime('\"%y-%m-%d\"')
    conn = sqlite3.connect('database/%s.db' % dbname)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS %s
        (CODE TEXT PRIMARY KEY UNIQUE,
        NAME   TEXT,
        PRICE  TEXT,
        AVERAGE  TEXT,
        K  TEXT,
        D  TEXT,
        J  TEXT,
        TIME   TEXT,
        TIMECROSS   TEXT,
        MARKET   TEXT);''' % date)
    conn.commit()
    conn.close()
    print("Form %s Created in %s!" % (date, dbname))

# 在数据库'KDJ'，表'17-12-27'中 写入 / CODE/ NAME/ PRICE/ AVERAGE/ K/ D/ J/ TIME/ TIMECROSS/ MARKET
def insert_ma_data(code, kdj):
    prices = price_now(code)
    price = str(prices[0])
    average = str(prices[1])
    name = share_name(code)
    K = kdj[0]
    D = kdj[1]
    J = kdj[2]
    time = datetime.now(timezone('Asia/Shanghai')).strftime('%H:%M:%S')
    formname = datetime.now(timezone('Asia/Shanghai')).strftime('\"%y-%m-%d\"')
    conn = sqlite3.connect('database/KDJ.db')
    c = conn.cursor()
    print(code, name, price, average, time)
    c.execute("INSERT OR IGNORE INTO %s (CODE, NAME, PRICE, AVERAGE, K, D, J, TIME, MARKET) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)" % formname, (code, name, price, average, K, D, J, time, share_market(code)))
    conn.commit()
    conn.close()
    print('写入 %s 数据成功！' % code)



def help():
    print('''
    start(list, debug=1)
    monitor_status = False
    stop()
      kdj_monitor(l, debug=0)
        kdj_checker(code)
    create_ma_form(dbname)
    insert_ma_data(code, kdj)
    help()
    ''')
