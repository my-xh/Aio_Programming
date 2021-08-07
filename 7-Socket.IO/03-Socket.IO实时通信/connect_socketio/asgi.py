# -*- coding: utf-8 -*-

"""
@File    : asgi.py
@Time    : 2021/8/8 16:24
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import os

import socketio

APP_ROOT = os.path.dirname(__file__)

sio_server = socketio.AsyncServer(
    # 配置该服务器的异步模式为ASGI
    async_mode='asgi',
    # 配置该服务器允许来自所有域的连接
    cors_allowed_origins='*',
)


@sio_server.on('my_event')
async def my_event(sid, data):
    """
    侦听浏览器的my_event事件，并向该连接发送my_event_callback事件

    :param sid: session ID
    :param data: 通过该事件传来的数据
    :return:
    """
    await sio_server.emit('my_event_callback', to=sid)


# @sio_server.on('login')
@sio_server.event
async def login(sid, data):
    """
    侦听浏览器的login事件

    :param sid: session ID
    :param data: 通过该事件传来的数据
    :return: 浏览器回调函数的参数
    """
    name = data.get('name', '')
    return f'Hello {name}, you are granted!'


app = socketio.ASGIApp(
    sio_server,
    static_files={
        '/static': os.path.join(APP_ROOT, 'static')
    },
)
