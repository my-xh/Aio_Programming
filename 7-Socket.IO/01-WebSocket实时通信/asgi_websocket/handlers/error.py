# -*- coding: utf-8 -*-

"""
@File    : error.py
@Time    : 2021/8/7 23:00
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 发送错误信息
"""


async def send_404_error(scope, receive, send):
    await send({
        'type': 'http.response.start',
        'status': 404,
        'headers': [
            (b'Content-Type', b'text/html'),
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': b'Not Found',
        'more_body': False
    })
