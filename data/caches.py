#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 21:43:40
# Filename        : data/caches.py
# Description     : 
from .model import RedisModel

class Cache(RedisModel):
    def find_key(self, key):
        return self.db.hgetall('cache_' + key)

    def attributes(self):
        return ['result', 'key', 'expired']

class Page(Cache):
    def attributes(self):
        return ['key', 'expired', 'headers', 'chunk', 'status']
    
    def find_key(self, key):
        _value = {}
        for k, v in self.db.hgetall('cache_' + key).iteritems():
            if k in ('headers', 'chunk', 'status'):
                _value[k] = eval(v, {})
            else:
                _value[k] = v

        return _value

