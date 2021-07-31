# -*- coding: utf-8 -*-

"""
@File    : asgi.py
@Time    : 2021/8/1 2:11
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""


async def app(scope, receive, send):
    conn_type = scope['type']
    if conn_type == 'http':
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                (b'Content-Type', b'text/html'),
            ]
        })
        await send({
            'type': 'http.response.body',
            'body': b'Hello World',
            'more_body': False
        })
    elif conn_type == 'lifespan':
        while True:
            message = await receive()
            if message['type'] == 'lifespan.startup':
                print('正在进行初始化操作...')
                await send({'type': 'lifespan.startup.complete'})
            elif message['type'] == 'lifespan.shutdown':
                print('正在进行收尾工作...')
                await send({'type': 'lifespan.shutdown.complete'})
                break
    else:
        raise NotImplementedError()
