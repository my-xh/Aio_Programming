# -*- coding: utf-8 -*-

"""
@File    : 03-multi_app.py
@Time    : 2021/8/7 16:11
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
from tornado import web
from tornado.ioloop import IOLoop
from tornado.routing import PathMatches, Rule, RuleRouter


class HanlderInApp1(web.RequestHandler):

    async def get(self):
        self.write('Handler in app1')
        await self.finish()


class HanlderInApp2(web.RequestHandler):

    async def get(self):
        self.write('Handler in app2')
        await self.finish()


if __name__ == '__main__':
    app1 = web.Application(
        handlers=[
            ('/app1/handler', HanlderInApp1),
        ]
    )
    app2 = web.Application(
        handlers=[
            ('/app2/handler', HanlderInApp2),
        ]
    )
    server = web.HTTPServer(
        RuleRouter([
            Rule(PathMatches('/app1.*'), app1),
            Rule(PathMatches('/app2.*'), app2),
        ])
    )
    server.listen(8888)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('HTTP Server stopped')
