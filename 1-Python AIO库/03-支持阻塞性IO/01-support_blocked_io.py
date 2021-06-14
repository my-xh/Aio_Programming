# -*- coding: utf-8 -*-

"""
@File    : 01-support_blocked_io.py
@Time    : 2021/6/13 22:06
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio
import time


def blocked_task():
    for i in range(10):
        time.sleep(1)
        print(f'[{time.strftime("%X")}] BLocked task {i}')


async def async_task():
    for i in range(2):
        await asyncio.sleep(5)
        print(f'[{time.strftime("%X")}] Async task {i}')


async def main():
    # 获取当前正在运行的事件循环对象
    current_running_loop = asyncio.get_running_loop()
    # 并发执行一个阻塞型任务和一个异步任务
    await asyncio.gather(
        # 让指定函数运行在特定的执行器中, None表示默认的线程池执行器
        current_running_loop.run_in_executor(None, blocked_task),
        async_task(),
    )


asyncio.run(main())
