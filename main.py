#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: main.py

import checktime

from sharelist_t import share_list
import sort_price
import sort_kdj

share_list = sort_price.sort_list(share_list)
share_list = sort_kdj.sort_list(share_list)

from monitor import *
ma_monitor_start(share_list, last_ma)


import code
code.interact(banner = "", local = locals())
