# -*- coding: utf-8 -*-

"""
@File    : aio_http_server.py
@Time    : 2021/6/14 12:01
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio


async def handle_connection(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    content = b'<html>' \
              b'<head>' \
              b'<title>Title</title>' \
              b'</head>' \
              b'<body>' \
              b'Hello World' \
              b'</body>' \
              b'</html>'
    # 设置HTTP响应状态, 200表示成功
    writer.write(b'HTTP/1.0 200 OK\r\n')
    # 指定HTTP响应内容的长度
    writer.write(f'Content-Length: {len(content)}\r\n'.encode())
    # 指定HTTP响应内容的格式
    writer.write(b'Content-Type: text/html\r\n')
    # 发送HTTP协议头结束标识
    writer.write(b'\r\n')
    # 发送响应内容
    writer.write(content)
    # 等待发送完成
    await writer.drain()
    # 关闭连接
    writer.close()


async def main():
    # 配置服务器端口
    async with await asyncio.start_server(
            handle_connection,
            port=8888,
    ) as server:
        # 启动服务器
        await server.serve_forever()


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        print('User stopped server')
