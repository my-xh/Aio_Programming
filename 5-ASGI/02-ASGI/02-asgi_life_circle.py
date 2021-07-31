# -*- coding: utf-8 -*-

"""
@File    : 02-asgi_life_circle.py
@Time    : 2021/8/1 1:57
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""


async def app(scope, receive, send):
    conn_type = scope['type']
    if conn_type == 'lifespan':
        while True:
            message = await receive()
            if message['type'] == 'lifespan.startup':
                print('正在进行初始化...')
                await send({
                    'type': 'lifespan.startup.complete',
                })
            elif message['type'] == 'lifespan.shutdown':
                print('正在进行收尾工作...')
                await send({
                    'type': 'lifespan.shutdown.complete',
                })
                break
