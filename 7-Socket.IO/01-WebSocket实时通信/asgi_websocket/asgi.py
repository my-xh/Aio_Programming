# -*- coding: utf-8 -*-

"""
@File    : asgi.py
@Time    : 2021/8/7 23:00
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : ASGI接口
"""
from handlers import handle_home_page_request, handle_lifespan, handle_ws_conn
from handlers.error import send_404_error


async def app(scope, receive, send):
    conn_type = scope['type']
    if conn_type == 'http':
        # http请求
        req_path = scope['path']
        if req_path == '/':
            # 处理网站根路径的请求
            await handle_home_page_request(scope, receive, send)
        else:
            # 对于其他路径的请求，均向浏览器发送404错误
            await send_404_error(scope, receive, send)
    elif conn_type == 'websocket':
        # WebSocket请求
        await handle_ws_conn(scope, receive, send)
    elif conn_type == 'lifespan':
        # 生命周期类型的请求
        await handle_lifespan(scope, receive, send)
    else:
        raise NotImplementedError()
