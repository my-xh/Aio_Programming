# -*- coding: utf-8 -*-

"""
@File    : server.py
@Time    : 2021/8/8 20:15
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio
import os
import time

import socketio
from tornado import web
from tornado.ioloop import IOLoop

APP_ROOT = os.path.dirname(__file__)

# 配置socketio>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 创建socketio服务器，配置异步模式为tornado
sio_server = socketio.AsyncServer(async_mode='tornado')


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


# 配置tornado>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class HomePage(web.RequestHandler):

    async def get(self):
        # 将该页面重定向到/static/index.html页面
        self.redirect('/static/index.html')


if __name__ == '__main__':
    app = web.Application(
        handlers=[
            # 配置根路径路由
            ('/', HomePage),
            # 配置静态文件目录
            ('/static/(.*)', web.StaticFileHandler, dict(path=os.path.join(APP_ROOT, 'static'))),
            # 将socketio应用映射到/socket.io/路径
            ('/socket.io/', socketio.get_tornado_handler(sio_server)),
        ]
    )
    try:
        app.listen(8000)
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('HTTP Server Stopped')
