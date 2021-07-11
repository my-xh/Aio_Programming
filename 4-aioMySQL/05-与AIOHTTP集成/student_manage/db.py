# -*- coding: utf-8 -*-

"""
@File    : db.py
@Time    : 2021/7/25 23:48
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import config

from aiomysql.sa import create_engine, Engine

file_scope_vars = {}


async def get_engine():
    """
    :return: 数据库引擎（单例）
    """
    if 'engine' not in file_scope_vars:
        file_scope_vars['engine'] = await create_engine(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            db=config.DB_NAME,
        )
    return file_scope_vars['engine']


def with_db(func):
    """
    给请求处理函数添加数据库支持

    :param func: 请求处理函数
    :return: 响应结果
    """

    async def wrapper(req):
        engine: Engine = await get_engine()
        async with engine.acquire() as conn:
            result = await func(req, conn)
        return result

    return wrapper
