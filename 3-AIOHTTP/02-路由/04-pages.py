# -*- coding: utf-8 -*-

"""
@File    : 04-pages.py
@Time    : 2021/6/19 23:30
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 获取URL参数
"""
from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request: web.Request):
    return web.Response(text="Hello, world")


@routes.get(r'/p/{page_id:\d+}')
async def page(request: web.Request):
    return web.Response(text=f'Page id is {request.match_info["page_id"]}')


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
