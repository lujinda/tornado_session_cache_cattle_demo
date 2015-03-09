#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 21:26:39
# Filename        : data/model.py
# Description     : 
from data.db import cache_db

class RedisModel(dict):
    def __init__(self):
        self['_record'] = {} # 在这里记录cache的信息

    def record(self):
        return self['_record']

    @property
    def db(self):
        return cache_db

    def attributes(self):
        raise NotImplementedError

    def __setattr__(self, key, value):
        assert key in self.attributes()
        self.record()[key] = value

    def __getattr__(self, key):
        assert key in self.attributes()
        return self.record().get('key', None)

    def save(self):
        key = 'cache_' + self.record().pop('key')
        expired = self.record().pop('expired', 7200)
        for k, v in self.record().iteritems():
            self.db.hset(key, k ,v)

        self.db.expire(key, expired)

    def flush(self):
        print self.db.keys('cache_*')


