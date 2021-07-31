# -*- coding: utf-8 -*-

"""
@File    : 01-simple_asgi.py
@Time    : 2021/8/1 1:28
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""


async def app(scope, receive, send):
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'Content-Type', b'text/plain'],
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello World',
        'more_body': False
    })
