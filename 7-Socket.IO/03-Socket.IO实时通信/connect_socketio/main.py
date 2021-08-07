# -*- coding: utf-8 -*-

"""
@File    : main.py
@Time    : 2021/8/8 16:30
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import os

if __name__ == '__main__':
    try:
        os.system('uvicorn asgi:app')
    except KeyboardInterrupt:
        pass
