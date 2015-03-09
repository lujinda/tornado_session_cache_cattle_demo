#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 21:35:55
# Filename        : data/config.py
# Description     : 

from ConfigParser import ConfigParser

class Config():
    def __init__(self):
        cfg_file = 'config.cfg'
        self.cfg = ConfigParser()
        self.cfg.read(cfg_file)

    def get_redis_config(self):
        return self.__get_config('redis', ['port', 'db'])

    def get_qiniu_config(self):
        return self.__get_config('qiniu')

    def __get_config(self, section, int_list = []):
        _d = {}
        for key, value in self.cfg.items(section):
            _d[key] = key in int_list and int(value) or value

        return _d

config  = Config()

redis_config = config.get_redis_config()
qiniu_config  = config.get_qiniu_config()

