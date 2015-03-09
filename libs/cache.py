#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 22:21:02
# Filename        : libs/cache.py
# Description     : 
try:
    import cPickle as pickle
except ImportError:
    import pickle as pickle

from data.caches import Cache, Page
from decorator import decorator
from tornado.escape import utf8
from hashlib import md5

def cache(expired = 7200, key = None):
    def wrap(func, self, *args, **kwargs):
        _key = key or (func.__name__ + self.__class__.__name__ + self.__module__)
        _key = key_gen(_key, args, kwargs)
        cache = Cache()
        cache_data = cache.find_key(_key)
        if cache_data:
            return pickle.loads(cache_data['result'])
        else:
            result = func(self, *args, **kwargs)
            cache.expired = expired
            cache.key = _key
            cache.result = pickle.dumps(result)
            cache.save()
            return result

    return decorator(wrap)

def page(expired = 7200, key = None):
    def wrap(method, self, *args, **kwargs):
        _key = key or self.request.uri

        cache = Page()
        cache_data = cache.find_key(_key)

        if cache_data and (cache_data['status'] in (200, 304)) and  cache_data['chunk']:
            headers = cache_data['headers']
            self.set_status(cache_data['status'])
            self._headers['Content-Type'] = headers['Content-Type']
            self._headers['Set-Cookie'] = headers.get('Set-Cookie', '')
            self.write(utf8(''.join(cache_data['chunk'])))
        else:
            method(self, *args, **kwargs)
            if not self._finished:
                self.finish()
            cache.key = _key
            cache.expired = expired
            cache.status = self._status_code
            cache.headers = self._headers
            cache.chunk = self._buffer
            cache.save()

    return decorator(wrap)

def key_gen(key, args, kwargs):
    code = md5(key)
    map(lambda x: code.update(str(x)), args)
    
    map(lambda k,v: code.update(str(k) + '=' + str(v)), kwargs.iteritems())

    return code.hexdigest()
    
