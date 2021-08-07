# -*- coding: utf-8 -*-

"""
@File    : websocket_connect.py
@Time    : 2021/8/7 23:16
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 处理WebSocket类型的请求
"""


async def handle_ws_conn(scope, receive, send):
    while True:
        msg = await receive()
        msg_type = msg['type']
        if msg_type == 'websocket.receive':
            # 接收WebSocket请求
            if msg['text'] == 'Ping':
                await send({
                    'type': 'websocket.send',
                    'text': 'Pong'
                })
        elif msg_type == 'websocket.connect':
            # 建立WebSocket连接
            print('Client Connect')
            await send({'type': 'websocket.accept'})
        elif msg_type == 'websocket.disconnect':
            # 断开WebSocket连接
            print('Client DisConnect')
            break
