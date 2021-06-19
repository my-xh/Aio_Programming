# -*- coding: utf-8 -*-

"""
@File    : 01-aiohttps.py
@Time    : 2021/7/11 1:13
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import os
import ssl

from aiohttp import web

APP_ROOT = os.path.dirname(__file__)

routes = web.RouteTableDef()


@routes.get('/')
async def index(req: web.Request):
    return web.Response(text='Hello, World')


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # 加载网站证书文件
    ssl_context.load_cert_chain(
        os.path.join(APP_ROOT, 'ssl', 'cert.pem'),
        os.path.join(APP_ROOT, 'ssl', 'cert.key'),
    )
    web.run_app(app, port=443, ssl_context=ssl_context)
