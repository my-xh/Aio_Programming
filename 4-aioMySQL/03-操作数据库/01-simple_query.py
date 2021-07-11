# -*- coding: utf-8 -*-

"""
@File    : 01-simple_query.py
@Time    : 2021/7/11 20:05
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import aiomysql
import asyncio


async def main():
    async with aiomysql.create_pool(
            maxsize=10,
            host='127.0.0.1',
            port=8306,
            user='root',
            password='pwd',
            db='mydb',
    ) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(
                    "SELECT * FROM `student`"
                    "WHERE `id` = 1;"
                )
                print(await cursor.fetchall())


if __name__ == '__main__':
    asyncio.run(main())
