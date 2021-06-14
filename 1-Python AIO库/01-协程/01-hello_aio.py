# -*- coding: utf-8 -*-

"""
@File    : 01-hello_aio.py
@Time    : 2021/6/13 21:51
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    :
"""
import asyncio
import time


async def main():
    print(f'{time.strftime("%X")} Hello')
    await asyncio.sleep(1)
    print(f'{time.strftime("%X")} Hello')


asyncio.run(main())
