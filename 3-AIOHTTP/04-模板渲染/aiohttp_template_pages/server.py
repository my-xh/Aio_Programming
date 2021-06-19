# -*- coding: utf-8 -*-

"""
@File    : server.py
@Time    : 2021/7/4 22:05
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
        request=request,
    )


@routes.get('/news')
@aiohttp_jinja2.template('news.html')
async def news(request: web.Request):
    return dict(
        title='动态',
        request=request,
    )


@routes.get('/blog')
@aiohttp_jinja2.template('blog.html')
async def blog(request: web.Request):
    return dict(
        title='博客',
        request=request,
        posts=[
            {'title': '文章1', 'content': '内容1'},
            {'title': '文章2', 'content': '内容2'},
        ]
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
