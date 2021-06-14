# -*- coding: utf-8 -*-

"""
@File    : 01-cpu_bound_computing.py
@Time    : 2021/6/13 22:32
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio
import concurrent.futures
import time

from numba import jit


# 通过JIT加速，先将代码编译成机器码再执行
@jit
def compute_pi():
    count = 100000
    part = 1 / count
    inside = 0

    for i in range(1, count):
        for j in range(1, count):
            x = i * part
            y = j * part
            if x ** 2 + y ** 2 <= 1:
                inside += 1

    return 4 * inside / (count * count)


async def print_pi(executor):
    print(f'[{time.strftime("%X")}] Started to compute PI')
    pi = await asyncio.get_running_loop().run_in_executor(
        executor,
        compute_pi,
    )
    print(f'[{time.strftime("%X")}] {pi}')


async def task():
    for i in range(5):
        print(f'[{time.strftime("%X")}] Step {i}')
        await asyncio.sleep(1)


async def main():
    # 创建进程池执行器
    executor = concurrent.futures.ProcessPoolExecutor()

    await asyncio.gather(
        print_pi(executor),
        task(),
    )


if __name__ == '__main__':
    asyncio.run(main())
