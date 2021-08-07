# -*- coding: utf-8 -*-

"""
@File    : 01-static_resource.py
@Time    : 2021/6/27 23:59
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
from aiohttp import web
import os

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text='Hello, world')


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    # 配置静态文件目录
    app.router.add_static(
        '/static',
        os.path.join(os.path.dirname(__file__), 'static')
    )
    web.run_app(app)
