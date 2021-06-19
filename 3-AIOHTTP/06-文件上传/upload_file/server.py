# -*- coding: utf-8 -*-

"""
@File    : server.py
@Time    : 2021/7/5 23:19
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import aiohttp_jinja2
import jinja2
import os

from datetime import datetime
from aiohttp import web

from aiofile import async_open

APP_ROOT = os.path.dirname(__file__)

routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template('index.html')
async def index(request: web.Request):
    return dict(title='首页')


@routes.post('/upload')
@aiohttp_jinja2.template('upload.html')
async def upload(request: web.Request):
    # 解析前端上传的数据
    data = await request.post()
    # 从解析数据中获取文件对象
    file_obj = data['file']
    # 以当前时间戳作为文件名
    filename = f'{datetime.now().timestamp():.0f}'
    # 将文件对象中的内容写入目标文件中
    async with async_open(
            os.path.join(APP_ROOT, 'uploads', filename), 'wb') as f:
        await f.write(file_obj.file.read())
    # 将文件在网站中的路径传给模板
    return dict(
        title='上传结果',
        file_path=f'/uploads/{filename}',
    )


if __name__ == '__main__':
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(
            os.path.join(APP_ROOT, 'templates')
        ),
    )
    app.add_routes(routes)
    app.router.add_static(
        '/node_modules',
        os.path.join(APP_ROOT, 'node_modules'),
    )
    app.router.add_static(
        '/uploads',
        os.path.join(APP_ROOT, 'uploads'),
    )
    web.run_app(app)
