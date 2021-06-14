# -*- coding: utf-8 -*-

"""
@File    : 01-aio_socket_server.py
@Time    : 2021/6/14 10:25
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio


async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    """
    向客户端发送5段数据，时间间隔为1s，之后关闭客户端连接
    :param reader: StreamReader对象，用于读取客户端传来的数据
    :param writer: StreamWriter对象，用于向客户端发送数据
    """
    for i in range(1, 6):
        writer.write(f'Count {i}\r\n'.encode())
        # 发送并等待数据发送成功
        await writer.drain()
        await asyncio.sleep(1)

    writer.close()


async def main():
    port = 8888
    # 启动服务器并注册一个回调函数用于侦听客户端连接
    server = await asyncio.start_server(
        # 客户端连接的回调函数
        handle_echo,
        port=port,
    )
    print(f'Server on port {port}')
    async with server:
        # 开始接受连接
        await server.serve_forever()


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        print('User stopped server')
