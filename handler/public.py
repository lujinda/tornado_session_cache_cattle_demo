#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 22:20:03
# Filename        : handler/public.py
# Description     : 

from tornado.web import RequestHandler
from libs.session import Session
from copy import deepcopy

class PublicHandler(RequestHandler):
    def valid_user(self):
        """
        返回当前用户是否是有效的
        """
        return self.session.get('username')

    def initialize(self):
        self.session = Session(self.application.session_manager, self)
        self.init_data()

    def init_data(self):
        pass

    def flush(self, *args, **kwargs):
        self._buffer = deepcopy(self._write_buffer)
        super(PublicHandler, self).flush(*args, **kwargs)

class BaseHandler(PublicHandler):
    def check_username_password(self, username, password):
        return username == 'test' and password == 'test'

class ApiBaseHandler(BaseHandler):
    def init_data(self):
        self.result_json = {
                'error': '', 'status_code': 200,
                'result': []
                }

    def send_result_json(self):
        result_json = self.__dict__.get('result_json')
        if isinstance(result_json, dict):
            self.write(result_json)
        else:
            assert AttributeError

    def write_error(self, status_code, **kwargs):
        try:
            self.result_json['error'] = kwargs['exc_info'][1].log_message
        except:
            self.result_json['error'] = 'unknown'
        self.result_json['status_code'] = status_code
        self.write(self.result_json)
        self.finish()


