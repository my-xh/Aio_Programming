# -*- coding: utf-8 -*-

"""
@File    : 02-aiomysql_crud.py
@Time    : 2021/7/11 20:12
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import aiomysql
import asyncio


# 打印查询的所有数据
async def print_all_data(cur: aiomysql.Cursor):
    await cur.execute(
        "SELECT * FROM `student`"
        "WHERE id > 0;"
    )
    # 获取原始数据结果
    raw_data = await cur.fetchall()
    # 计算字段个数
    field_range = range(len(cur.description))
    # 将字段名与原始数据结果映射成对象数组
    data = [
        {cur.description[i][0]: row[i] for i in field_range}
        for row in raw_data
    ]
    print(data)


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
            async with conn.cursor() as cur:
                await print_all_data(cur)
                # 修改数据
                await cur.execute(
                    "UPDATE `student` SET "
                    "`name` = '小云加',"
                    "`age` = 12 "
                    "WHERE `id` = 1;"
                )
                await print_all_data(cur)
                # 删除数据
                await cur.execute(
                    "DELETE FROM `student`"
                    "WHERE `id` = 2;"
                )
                await print_all_data(cur)
                # 提交更改到数据库
                await conn.commit()


if __name__ == '__main__':
    asyncio.run(main())
