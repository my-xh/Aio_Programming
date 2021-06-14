# -*- coding: utf-8 -*-

"""
@File    : 01-aio_multi_task.py
@Time    : 2021/6/13 21:53
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio
import time


async def task(tag, delay):
    for i in range(6):
        await asyncio.sleep(delay)
        print(f'[{time.strftime("%X")}]Task:{tag}, step {i}')


async def main():
    asyncio.create_task(task('task1', 1))
    await asyncio.create_task(task('task2', 2))  # 等待该任务完成


asyncio.run(main())
