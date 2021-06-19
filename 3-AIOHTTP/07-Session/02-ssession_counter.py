# -*- coding: utf-8 -*-

"""
@File    : 02-ssession_counter.py
@Time    : 2021/7/6 22:57
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    :
"""
import base64

from aiohttp import web
from aiohttp_session import get_session, setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet

routes = web.RouteTableDef()


@routes.get('/')
async def index(request: web.Request):
    session = await get_session(request)
    session['count'] = (session['count'] if 'count' in session else 0) + 1
    return web.Response(text=f'Count is {session["count"]}')


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    fernet_key = fernet.Fernet.generate_key()
    # secret_key必须是url安全的、base64编码的32位字节数据
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(
        app,
        EncryptedCookieStorage(secret_key),
    )
    web.run_app(app)
