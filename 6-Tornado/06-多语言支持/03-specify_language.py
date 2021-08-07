# -*- coding: utf-8 -*-

"""
@File    : 03-specify_language.py
@Time    : 2021/8/7 19:14
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
        # 根据URL中的lang参数确定页面语言
        # 指定中文：localhost:8888?lang=zh_CN
        self.locale = locale.get(self.get_query_argument('lang', 'en_US'))
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
