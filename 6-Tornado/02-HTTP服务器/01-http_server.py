# -*- coding: utf-8 -*-

"""
@File    : 01-http_server.py
@Time    : 2021/8/7 14:11
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
from tornado import web
from tornado.ioloop import IOLoop


class HomePage(web.RequestHandler):

    async def get(self):
        self.write('Hello World')
        await self.finish()  # 必须手动调用才能实现异步非阻塞

    async def post(self):
        self.write('Handle post request')
        await self.finish()


if __name__ == '__main__':
    app = web.Application(
        handlers=[
            # 配置网站根路径的请求处理器
            ('/', HomePage),
        ]
    )
    app.listen(8888)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('HTTP Server Stopped')
