#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: main.py


from sharelist_t import share_list

from checktime import check_time

check_time(9,25,0)

import sort_price
import sort_kdj

share_list = sort_price.sort_list(share_list)
share_list = sort_kdj.sort_list(share_list)

from monitor import *

check_time(9,30,1)

start(share_list, 0)


import code
code.interact(banner = "", local = locals())
