# -*- coding: utf-8 -*-

"""
@File    : 01-write_file.py
@Time    : 2021/6/13 23:56
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio


async def main():
    loop = asyncio.get_running_loop()
    f = await loop.run_in_executor(None, open, 'data.txt', 'w')
    await loop.run_in_executor(None, f.write, 'aio file')
    await loop.run_in_executor(None, f.close)


asyncio.run(main())
