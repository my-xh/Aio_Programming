# -*- coding: utf-8 -*-

"""
@File    : 01-template_render.py
@Time    : 2021/7/4 21:01
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
async def hello(request):
    return dict(name='小云', age=20)


if __name__ == '__main__':
    app = web.Application()
    # 指定模板文件根目录，将模板系统与服务端应用集成
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(
            os.path.join(os.path.dirname(__file__), 'templates')
        ),
    )
    app.add_routes(routes)
    web.run_app(app)
