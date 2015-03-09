#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 19:29:07
# Filename        : libs/wrap.py
# Description     : 
from functools import wraps
from tornado.web import HTTPError

def api_authenticated(method):
    @wraps(method)
    def wrap(self, *args, **kwargs):
        if self.valid_user():
            result = method(self, *args, **kwargs)
            return result
        else:
            raise HTTPError(500, '用户验证出错')

    return wrap

def authenticated(method):
    @wraps(method)
    def wrap(self, *args, **kwargs):
        if self.valid_user():
            result = method(self, *args, **kwargs)
            return result
        else:
            self.set_status(301)
            login_url = self.get_login_url()
            if '?' in login_url:
                joiner = '&'
            else:
                joiner = '?'

            url = login_url + joiner + 'callback_url=' + self.request.uri

            self.redirect(url)

    return wrap


