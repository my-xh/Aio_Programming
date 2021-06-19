# -*- coding: utf-8 -*-

"""
@File    : 03-config_route_with_decorator.py
@Time    : 2021/6/19 23:28
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 通过装饰器配置路由
"""
from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request: web.Request):
    return web.Response(text="Hello, world")


@routes.post('/save_user_info')
async def save_user_info(request):
    return web.Response(text='Saved')


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
