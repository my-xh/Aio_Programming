# -*- coding: utf-8 -*-

"""
@File    : 01-session_counter.py
@Time    : 2021/7/6 22:48
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import aiohttp_session

from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def index(request: web.Request):
    session = await aiohttp_session.get_session(request)
    session['count'] = (session['count'] if 'count' in session else 0) + 1
    return web.Response(text=f'Count is {session["count"]}')


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    # 配置Session
    aiohttp_session.setup(
        app,
        aiohttp_session.SimpleCookieStorage(),
    )
    web.run_app(app)
