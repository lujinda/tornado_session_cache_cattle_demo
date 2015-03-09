#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-08 14:54:17
# Filename        : run.py
# Description     : 
from app import DemoApplication
from tornado import ioloop, httpserver, options
from tornado.options import options, define

define('port', default = 1234, type = int, help = 'listen port')

def main():
    options.parse_command_line()
    app = DemoApplication()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

