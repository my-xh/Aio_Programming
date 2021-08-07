# -*- coding: utf-8 -*-

"""
@File    : asgi.py
@Time    : 2021/8/8 15:53
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import os

import socketio

APP_ROOT = os.path.dirname(__file__)

# 创建一个AsyncServer实例
sio_server = socketio.AsyncServer()

# 创建一个asgi应用
app = socketio.ASGIApp(
    socketio_server=sio_server,
    # 配置静态文件目录，使用Socket.IO内置的静态文件服务器处理静态请求
    static_files={
        '/static': os.path.join(APP_ROOT, 'static')
    },
)
