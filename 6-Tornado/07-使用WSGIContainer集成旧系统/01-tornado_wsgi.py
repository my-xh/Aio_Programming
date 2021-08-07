# -*- coding: utf-8 -*-

"""
@File    : 01-tornado_wsgi.py
@Time    : 2021/8/7 21:17
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
from tornado import web
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from web2py import wsgihandler

if __name__ == '__main__':
    # 创建一个WSGI容器，用于支持WSGI应用
    wsgi_container = WSGIContainer(wsgihandler.application)
    server = web.HTTPServer(wsgi_container)
    server.listen(8888)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('HTTP Server Stopped')
