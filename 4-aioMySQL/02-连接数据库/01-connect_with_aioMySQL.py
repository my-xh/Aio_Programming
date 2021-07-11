# -*- coding: utf-8 -*-

"""
@File    : 01-connect_with_aioMySQL.py
@Time    : 2021/7/11 15:37
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import aiomysql
import asyncio


async def main():
    # 建立与数据库的连接
    # conn: aiomysql.Connection
    async with aiomysql.connect(
            host='127.0.0.1',
            port=8306,
            user='root',
            password='pwd',
            db='mydb',
    ) as conn:
        # 创建游标用于操作数据库
        # cursor: aiomysql.Cursor
        async with conn.cursor() as cursor:
            # 执行一条SQL语句，返回受影响的数据条数
            effected = await cursor.execute(
                "INSERT INTO `student`(`name`, `age`)"
                "VALUES ('小云', 10);"
            )
            print(effected)
            # 提交更改到数据库
            await conn.commit()


if __name__ == '__main__':
    asyncio.run(main())
