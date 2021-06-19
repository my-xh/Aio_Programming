# -*- coding: utf-8 -*-

"""
@File    : 01-server.py
@Time    : 2021/6/16 22:49
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
from aiohttp import web


# 请求处理函数，接受一个参数作为请求对象，返回一个响应对象
async def hello(request: web.Request):
    return web.Response(text='Hello, world')


if __name__ == '__main__':
    # 创建一个服务器应用
    app = web.Application()
    # 将hello()处理函数映射到网站根路径
    app.router.add_get('/', hello)
    # 启动服务器应用
    web.run_app(app)
