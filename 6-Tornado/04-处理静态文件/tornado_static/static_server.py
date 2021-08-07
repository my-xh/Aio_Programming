# -*- coding: utf-8 -*-

"""
@File    : static_server.py
@Time    : 2021/8/7 16:36
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import os

from tornado import web
from tornado.ioloop import IOLoop

APP_ROOT = os.path.dirname(__file__)


class HomePage(web.RequestHandler):

    async def get(self):
        self.write('Hello World')
        await self.finish()


if __name__ == '__main__':
    app = web.Application(
        handlers=[
            (
                '/static/(.*)',
                web.StaticFileHandler,
                dict(path=os.path.join(APP_ROOT, 'static')),  # 配置静态文件目录
            ),
            ('/', HomePage),
        ]
    )
    app.listen(8888)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('HTTP Server stopped')
