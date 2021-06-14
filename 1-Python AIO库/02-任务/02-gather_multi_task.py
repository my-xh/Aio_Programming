# -*- coding: utf-8 -*-

"""
@File    : 02-gather_multi_task.py
@Time    : 2021/6/13 21:58
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
    # 并发执行多个任务
    await asyncio.gather(
        task("task1", 1),
        task("task2", 2),
    )


asyncio.run(main())
