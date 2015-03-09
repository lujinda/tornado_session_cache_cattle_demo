#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 19:57:52
# Filename        : app.py
# Description     : 
from tornado.web import Application
from handler.page import IndexHandler
from handler.user import LoginHandler, LogoutHandler
from handler.api import ApiBucketHandler
from data.db import session_db
from data.qiniu import cattle
from libs.session import SessionManager

import os

class DemoApplication(Application):
    def __init__(self):
        handlers = [
                (r'/', IndexHandler),
                (r'/login', LoginHandler),
                (r'/logout', LogoutHandler),
                (r'/api/bucket', ApiBucketHandler),
                ]

        settings = {
                'debug': True,
                'gzip': True,
                'static_path': os.path.join(os.path.dirname(__file__),
                    'static'),
                'template_path': os.path.join(os.path.dirname(__file__), 
                    'template'),
                'cookie_secret': '0a18b23b50ad427d93f7d1d562a446ea',
                'login_url': '/login',
                }

        session_settings = {
                'session_secret': '0a18b23b50ad427d93f7d1d562a446ea',
                'session_timeout': 6000,
                'session_db': session_db, # 使用redis来存session
                }

        self.session_manager = SessionManager(**session_settings)
        self.cattle = cattle 

        super(DemoApplication, self).__init__(handlers, **settings)


