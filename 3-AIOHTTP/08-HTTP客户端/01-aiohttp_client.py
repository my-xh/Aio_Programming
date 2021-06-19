# -*- coding: utf-8 -*-

"""
@File    : 01-aiohttp_client.py
@Time    : 2021/7/11 0:40
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import aiohttp
import asyncio
import time


async def main():
    async with aiohttp.ClientSession(
            # 使用最简单的Cookie机制
            cookie_jar=aiohttp.CookieJar(unsafe=True),
    ) as session:
        for i in range(10):
            response = await session.get('http://127.0.0.1:8080')  # 连接服务器
            print(f'[{time.strftime("%X")}] {await response.text()}')
            await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
