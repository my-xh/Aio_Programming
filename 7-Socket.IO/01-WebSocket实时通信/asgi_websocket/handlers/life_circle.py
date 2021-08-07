# -*- coding: utf-8 -*-

"""
@File    : life_circle.py
@Time    : 2021/8/7 23:03
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 处理生命周期类型的请求
"""


async def handle_lifespan(scope, receive, send):
    while True:
        msg = await receive()
        msg_type = msg['type']
        if msg_type == 'lifespan.startup':
            # 进行初始化工作
            await send({'type': 'lifespan.startup.complete'})
        elif msg_type == 'lifespan.shutdown':
            # 进行收尾工作
            await send({'type': 'lifespan.shutdown.complete'})
            break
