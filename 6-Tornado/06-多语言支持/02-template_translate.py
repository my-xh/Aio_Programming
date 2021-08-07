# -*- coding: utf-8 -*-

"""
@File    : 02-template_translate.py
@Time    : 2021/8/7 19:06
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import os

from tornado import web, locale
from tornado.ioloop import IOLoop

APP_ROOT = os.path.dirname(__file__)


class HomePage(web.RequestHandler):

    async def get(self):
        await self.render('index.html', greeting_word='Hello')


if __name__ == '__main__':
    # 从指定目录加载语言表
    locale.load_translations(os.path.join(APP_ROOT, 'languages'))
    app = web.Application(
        handlers=[
            ('/', HomePage),
        ],
        template_path=os.path.join(APP_ROOT, 'templates'),
    )
    app.listen(8888)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('HTTP Server Stopped')
