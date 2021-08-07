# -*- coding: utf-8 -*-

"""
@File    : server.py
@Time    : 2021/8/8 17:42
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import os

import socketio

APP_ROOT = os.path.dirname(__file__)

# 创建AsyncServer实例
sio_server = socketio.AsyncServer(async_mode='asgi')


@sio_server.event
async def msg(sid, data):
    username = data.get('username')
    content = data.get('content', '')
    if not username:
        username = sid[:5]
    # emit()的to参数为空时，向所有连接终端广播消息
    await sio_server.emit('msg', data={
        'from': username,
        'content': content,
    })


# 创建ASGIApp应用
app = socketio.ASGIApp(
    sio_server,
    socketio_path='/chatroom',  # 配置服务路径，默认为/socket.io
    static_files={
        '/static': os.path.join(APP_ROOT, 'static')
    }
)
