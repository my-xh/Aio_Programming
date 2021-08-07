# -*- coding: utf-8 -*-

"""
@File    : server.py
@Time    : 2021/8/7 22:00
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
from tornado import web
from tornado.ioloop import IOLoop


class HomePage(web.RequestHandler):

    async def get(self):
        name = self.get_query_argument('name', '')
        self.write(f'Hello, {name}')
        await self.finish()

    async def post(self):
        name = self.get_body_argument('name', '')
        self.write(f'Welcome, {name}')
        await self.finish()


if __name__ == '__main__':
    app = web.Application(
        handlers=[
            ('/', HomePage),
        ]
    )
    app.listen(8888)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('HTTP Server Stopped')
