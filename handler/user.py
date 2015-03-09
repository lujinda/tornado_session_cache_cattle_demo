#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 21:36:43
# Filename        : handler/user.py
# Description     : 

from .public import BaseHandler
from libs.wrap import authenticated
from libs import cache

class LoginHandler(BaseHandler):
    @property
    @cache.cache(expired = 7200)
    def home_page(self):
        """
        定义用户的主页
        """
        print 'in home_page'
        return '/' 

    def get(self):
        self.render('login.html')

    def post(self):
        """
        只做一些简单的验证了
        """
        username = self.get_argument('username')
        password = self.get_argument('password')

        assert username and password

        if self.check_username_password(username, password):
            self.session['username'] = username
            self.session['home_page'] = self.home_page
            self.session.save()

            redirect_url = self.get_query_argument('callback_url', self.session['home_page'])  # 登录成功后则重定向到登录前的页面或者用户主页
        else:
            redirect_url = self.request.uri

        self.redirect(redirect_url)

class LogoutHandler(BaseHandler):
    def get(self):
        self.session.logout()
        self.write('logout ok')

