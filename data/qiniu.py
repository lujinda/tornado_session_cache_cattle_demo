#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 18:59:44
# Filename        : data/qiniu.py
# Description     : 
from cattle.cattle import Cattle # 自己写的七牛第三方sdk
from config import qiniu_config

cattle = Cattle(**qiniu_config)

