# -*- coding: utf-8 -*-

"""
@File    : 02-write_with_aiofile.py
@Time    : 2021/6/14 0:09
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio
import time

from aiofile import async_open


async def main():
    # f = await async_open('data.txt', 'w')
    # await f.write('aio file')
    # await f.close()

    async with async_open('data.txt', 'w') as f:
        await f.write('aio file')


if __name__ == '__main__':
    asyncio.run(main())
