# -*- coding: utf-8 -*-

"""
@File    : config.py
@Time    : 2021/7/25 23:42
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import os

# 服务器根目录
SERVER_ROOT = os.path.dirname(__file__)

# 静态文件目录
STATIC_MAPPING = [
    dict(
        web_path='/node_modules',
        directory=os.path.join(SERVER_ROOT, 'node_modules'),
    ),
    dict(
        web_path='/static',
        directory=os.path.join(SERVER_ROOT, 'static'),
    ),
]

# 模板文件根目录
TEMPLATE_ROOT = os.path.join(SERVER_ROOT, 'templates')

# 数据库连接配置信息
DB_HOST = 'db'
DB_PORT = 3306
DB_NAME = 'mydb'
DB_USER = 'root'
DB_PASSWORD = 'pwd'
