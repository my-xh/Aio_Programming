# -*- coding: utf-8 -*-

"""
@File    : 01-aiomysql_sqlalchemy.py
@Time    : 2021/7/11 20:41
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import aiomysql
import aiomysql.sa
import aiomysql.sa.result
import aiomysql.sa.transaction
import asyncio
import sqlalchemy

# 声明数据库结构
student = sqlalchemy.Table(
    'student', sqlalchemy.MetaData(),
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(512)),
    sqlalchemy.Column('age', sqlalchemy.Integer),
)


# 打印查询的所有数据
async def print_all_data(conn: aiomysql.sa.connection.SAConnection):
    result: aiomysql.sa.result.ResultProxy = await conn.execute(
        student.select()
    )
    raw_data = await result.fetchall()
    # 将字段名和原始数据结果映射成对象数组
    data = [
        dict(row.items()) for row in raw_data
    ]
    print(data)


async def main():
    # 创建带连接池的数据库引擎
    engine: aiomysql.sa.Engine
    async with aiomysql.sa.create_engine(
            maxsize=10,
            host='127.0.0.1',
            port=8306,
            user='root',
            password='pwd',
            db='mydb',
    ) as engine:
        # 建立与SQLAlchemy的连接
        conn: aiomysql.sa.connection.SAConnection
        async with engine.acquire() as conn:
            # 开启事务处理
            trans: aiomysql.sa.transaction.Transaction = await conn.begin()
            try:
                # 增加一条数据
                await conn.execute(
                    student.insert().values(
                        name='小云',
                        age=10,
                    )
                )
                await print_all_data(conn)
                # 修改一条数据
                await conn.execute(
                    student.update().where(
                        student.c.id == 1
                    ).values(
                        name='小云加',
                        age=20,
                    )
                )
                await print_all_data(conn)
                # 删除一条数据
                await conn.execute(
                    student.delete().where(
                        student.c.id == 1
                    )
                )
                await print_all_data(conn)
            except:
                await trans.rollback()  # 回滚事务
            else:
                await trans.commit()  # 提交事务


if __name__ == '__main__':
    asyncio.run(main())
