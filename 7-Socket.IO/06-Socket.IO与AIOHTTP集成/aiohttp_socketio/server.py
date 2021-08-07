# -*- coding: utf-8 -*-

"""
@File    : server.py
@Time    : 2021/8/8 19:40
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio
import os
import time

import socketio
from aiohttp import web

APP_ROOT = os.path.dirname(__file__)

# 配置socketio>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 创建socketio服务器，配置异步模式为aiohttp
sio_server = socketio.AsyncServer(async_mode='aiohttp')


async def echo_task(sid):
    for i in range(6):
        # 每隔一秒向浏览器发送一条消息
        await sio_server.emit(
            event='echo',
            data=f'[{time.strftime("%X")}] Count: {i}',
            to=sid,
        )
        await asyncio.sleep(1)


# 重写connect连接事件处理
@sio_server.event
async def connect(sid, environ):
    asyncio.create_task(echo_task(sid))


# 配置aiohttp>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 声明路由表
routes = web.RouteTableDef()


# 配置根路径路由
@routes.get('/')
async def home_page(req):
    # 将页面重定向到/static/index.html页面
    return web.HTTPTemporaryRedirect('/static/index.html')


if __name__ == '__main__':
    app = web.Application()
    # 关联aiohttp服务器和socketio服务器
    sio_server.attach(app)
    # 配置路由
    app.add_routes(routes)
    # 配置静态文件目录
    app.router.add_static(
        '/static',
        os.path.join(APP_ROOT, 'static'),
    )
    print(os.path.join(APP_ROOT, 'static'))
    # 启动aiohttp服务器
    web.run_app(app)
