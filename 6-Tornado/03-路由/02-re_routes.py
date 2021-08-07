# -*- coding: utf-8 -*-

"""
@File    : 02-re_routes.py
@Time    : 2021/8/7 15:58
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
from tornado import web
from tornado.ioloop import IOLoop


class AppPage(web.RequestHandler):

    async def get(self, path_arg1, path_arg2):
        """
        该函数必须可以接收两个参数
        
        :param path_arg1: 正则表达式截取的第一个变量
        :param path_arg2: 正则表达式截取的第二个变量
        :return: 
        """
        self.write(f'Args1 is: {path_arg1}, Args2 is: {path_arg2}')
        await self.finish()


if __name__ == '__main__':
    app = web.Application(
        handlers=[
            # 通过正则表达式从路径中截取两个变量
            ('/app/(.*)/(.*)', AppPage),
        ]
    )
    app.listen(8888)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('HTTP server stopped')
