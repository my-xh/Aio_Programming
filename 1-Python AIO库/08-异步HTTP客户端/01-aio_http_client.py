# -*- coding: utf-8 -*-

"""
@File    : 01-aio_http_client.py
@Time    : 2021/6/14 11:38
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio


async def main():
    # 连接到服务器
    reader, writer = await asyncio.open_connection(
        "yunp.top",
        80,
    )
    # HTTP协议的第一行，指定请求资源及HTTP版本
    writer.write(b'GET / HTTP/1.0\r\n')
    # 发送HTTP协议头结尾标识
    writer.write(b'\r\n')
    # 等待数据发送成功
    await writer.drain()
    # 读取服务器返回的数据
    data = await reader.read()
    print(f'{data.decode()}')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
