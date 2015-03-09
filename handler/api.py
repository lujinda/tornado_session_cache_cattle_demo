#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 22:18:24
# Filename        : handler/api.py
# Description     : 
from .public import ApiBaseHandler
from libs.wrap import api_authenticated
from libs import cache

class ApiBucketHandler(ApiBaseHandler):
    @api_authenticated
    @cache.page(expired = 1000)
    def get(self):
        operation = self.get_query_argument('operation', 'list')
        do_func = getattr(self, 'do_' + operation, None)

        assert do_func
        do_func()
        self.send_result_json()

    def do_list(self):
        bucket = self.get_query_argument('bucket')
        self.result_json['result'] = self.application.cattle.ls_all(bucket)

