# -*- coding: utf-8 -*-

"""
@File    : asgi.py
@Time    : 2021/8/1 22:36
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route


async def index(request):
    return HTMLResponse('Hello Starlette')


app = Starlette(debug=True, routes=[Route('/', index)])
# app = Starlette()
# app.debug = True
# app.router.add_route('/', index)
