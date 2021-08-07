# -*- coding: utf-8 -*-

"""
@File    : 01-tcp_server.py
@Time    : 2021/8/7 13:41
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio
import time

from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError, IOStream
from tornado.tcpserver import TCPServer


class EchoServer(TCPServer):

    async def handle_stream(self, stream: IOStream, address: tuple):
        for i in range(6):
            try:
                data = f'[{time.strftime("%X")}] Count {i}\r\n'
                await stream.write(data.encode())
                await asyncio.sleep(1)
            except StreamClosedError:
                break


if __name__ == '__main__':
    server = EchoServer()
    server.listen(8888)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('TCP Server Stopped')

    # 终端测试: telnet 127.0.0.1 8888
