# -*- coding: utf-8 -*-

"""
@File    : wsgi_app.py
@Time    : 2021/8/1 0:40
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""


def application(environ, start_response):
    status = '200 OK'
    content = b'Hello World!'

    response_headers = [
        ('Content-Type', 'text/plain',),
        ('Content-Length', str(len(content))),
    ]

    start_response(status, response_headers)
    return [content]
