# -*- coding: utf-8 -*-

"""
@File    : 02-mix_tornado_and_wsgi.py
@Time    : 2021/8/7 21:45
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
from tornado import web
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from web2py import wsgihandler


class HomePage(web.RequestHandler):

    async def get(self):
        self.write('Home page')
        await self.finish()


if __name__ == '__main__':
    # 创建一个WSGI容器，用于支持WSGI应用
    wsgi_container = WSGIContainer(wsgihandler.application)
    app = web.Application(
        handlers=[
            ('/', HomePage),
            (
                '/welcome.*',
                web.FallbackHandler,  # 使用FallbackHandler将指定请求交由WSGI应用处理
                dict(fallback=wsgi_container)
            ),
        ]
    )
    app.listen(8888)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('HTTP Server Stopped')
