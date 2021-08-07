# -*- coding: utf-8 -*-

"""
@File    : 01-routes.py
@Time    : 2021/8/7 15:43
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
from tornado import web
from tornado.ioloop import IOLoop


class HomePage(web.RequestHandler):

    async def get(self):
        self.write('Home')
        await self.finish()


class Users(web.RequestHandler):

    async def get(self):
        self.write('Users')
        await self.finish()


class AppPage(web.RequestHandler):

    async def get(self):
        self.write(f'Request path is: {self.request.path}')
        await self.finish()


if __name__ == '__main__':
    app = web.Application(
        handlers=[
            ('/', HomePage),
            ('/users', Users),
            ('/app.*', AppPage),
        ]
    )
    app.listen(8888)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('HTTP Server Stopped')
