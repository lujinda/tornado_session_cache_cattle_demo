#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 19:58:16
# Filename        : data/db.py
# Description     : 

from redis import Redis
from .config import redis_config

cache_db = session_db = Redis(**redis_config)

