# -*- coding: utf-8 -*-

"""
@File    : 01-aio_socket_client.py
@Time    : 2021/6/14 10:46
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio
import time


async def main():
    # 连接到服务器
    reader, writer = await asyncio.open_connection(
        '127.0.0.1',
        8888,
    )
    # 通过循环逐行读取数据，直到读到数据结尾时退出循环
    while not reader.at_eof():
        # 读取一行数据
        data = await reader.readline()
        print(f'[{time.strftime("%X")}] Received {data}')


asyncio.get_event_loop().run_until_complete(main())
