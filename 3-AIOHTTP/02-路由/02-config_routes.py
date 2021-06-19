# -*- coding: utf-8 -*-

"""
@File    : 02-config_routes.py
@Time    : 2021/6/19 23:25
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 批量配置路由
"""
from aiohttp import web


async def hello(request: web.Request):
    return web.Response(text="Hello, world")


async def users(request):
    return web.Response(text='All users are here')


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([
        web.get('/', hello),
        web.get('/users', users),
    ])
    web.run_app(app)
