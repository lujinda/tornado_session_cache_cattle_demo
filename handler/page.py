#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 22:18:11
# Filename        : handler/page.py
# Description     : 
from .public import BaseHandler 
from libs.wrap import authenticated
from libs import cache

class IndexHandler(BaseHandler):
    @authenticated
    @cache.page(expired = 1000)
    def get(self):
        print 'in get no cache'
        self.render('index.html')

