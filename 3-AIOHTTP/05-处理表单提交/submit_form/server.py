# -*- coding: utf-8 -*-

"""
@File    : server.py
@Time    : 2021/7/4 23:08
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import aiohttp_jinja2
import jinja2
import os

from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template('index.html')
async def index(request: web.Request):
    return dict(
        title='首页',
    )


@routes.post('/login')
@aiohttp_jinja2.template('login.html')
async def login(request: web.Request):
    user = await request.post()
    return dict(
        title='登陆结果',
        user=user,
    )


if __name__ == '__main__':
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(
            os.path.join(os.path.dirname(__file__), 'templates')
        ),
    )
    app.add_routes(routes)
    app.router.add_static(
        '/node_modules',
        os.path.join(os.path.dirname(__file__), 'node_modules'),
    )
    web.run_app(app)
