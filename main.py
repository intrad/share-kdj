#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: main.py


from sharelist_t import share_list

import checktime

import sort_price
import sort_kdj

share_list = sort_price.sort_list(share_list)
share_list = sort_kdj.sort_list(share_list)

from monitor import *
start(share_list, 0)


import code
code.interact(banner = "", local = locals())
