# -*- coding: utf-8 -*-

"""
@File    : 02-connect_with_aioMySQL_pool.py
@Time    : 2021/7/11 16:25
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import aiomysql
import asyncio


async def main():
    # 创建一个连接池，允许的最大连接数为10
    # pool: aiomysql.Pool
    async with aiomysql.create_pool(
            maxsize=10,
            host='127.0.0.1',
            port=8306,
            user='root',
            password='pwd',
            db='mydb',
    ) as pool:
        # 通过连接池启用一个连接，如果当前连接池已满，则等待其他连接被释放后再建立连接
        # conn: aiomysql.Connection
        async with pool.acquire() as conn:
            # 创建游标用于操作数据库
            # cursor: aiomysql.Cursor
            async with conn.cursor() as cursor:
                effected = await cursor.execute(
                    "INSERT INTO `student`(`name`, `age`)"
                    "VALUES ('小红', 11);"
                )
                print(effected)
                # 提交更改到数据库
                await conn.commit()


if __name__ == '__main__':
    asyncio.run(main())
