# -*- coding: utf-8 -*-

"""
@File    : 01-template_render.py
@Time    : 2021/8/7 18:03
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import os

from tornado import web
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError

APP_ROOT = os.path.dirname(__file__)


class HomePage(web.RequestHandler):

    async def get(self):
        try:
            await self.render('index.html', title='首页')
        except StreamClosedError:
            pass


class Users(web.RequestHandler):

    async def get(self):
        try:
            await self.render('users.html', title='用户列表', users=['李明', '张亮'])
        except StreamClosedError:
            pass


if __name__ == '__main__':
    app = web.Application(
        handlers=[
            ('/', HomePage),
            ('/users', Users),
        ],
        template_path=os.path.join(APP_ROOT, 'templates')
    )
    app.listen(8888)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('HTTP Server Stopped')
