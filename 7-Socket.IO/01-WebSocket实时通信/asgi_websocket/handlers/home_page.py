# -*- coding: utf-8 -*-

"""
@File    : home_page.py
@Time    : 2021/8/7 23:01
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 处理主页请求
"""
import os

from aiofile import async_open
from settings import APP_ROOT


async def handle_home_page_request(scope, receive, send):
    # 向浏览器发送http响应头
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            (b'Content-Type', b'text/html'),
        ]
    })

    file_path = os.path.join(APP_ROOT, 'index.html')
    # 异步IO方式打开index.html, 并以二进制模式读取数据
    async with async_open(file_path, 'rb') as f:
        data = await f.read()

    # 向浏览器发送http响应体
    await send({
        'type': 'http.response.body',
        'body': data,
        'more_body': False
    })
