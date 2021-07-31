# -*- coding: utf-8 -*-

"""
@File    : asgi.py
@Time    : 2021/8/1 18:07
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""

from quart import Quart

# 创建一个Quart应用
app = Quart(__name__)


# 处理根路径的请求
@app.route('/')
async def index():
    return 'Hello Quart'


if __name__ == '__main__':
    app.run()
