# -*- coding: utf-8 -*-

"""
@File    : 01-client_get.py
@Time    : 2021/8/7 22:03
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio

from tornado.httpclient import AsyncHTTPClient

# 创建一个基于异步IO的HTTP客户端
client = AsyncHTTPClient()


async def main():
    # 向服务器发送一个GET请求
    resp = await client.fetch('http://127.0.0.1:8888?name=xh')
    # 将服务器返回的结果以utf-8的编码方式进行解码
    print(resp.body.decode('utf-8'))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
