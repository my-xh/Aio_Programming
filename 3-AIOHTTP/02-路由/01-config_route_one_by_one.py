# -*- coding: utf-8 -*-

"""
@File    : 01-config_route_one_by_one.py
@Time    : 2021/6/19 23:14
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 单独配置路由
"""
from aiohttp import web


async def hello(request: web.Request):
    return web.Response(text="Hello, world")


if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/', hello)
    web.run_app(app)
