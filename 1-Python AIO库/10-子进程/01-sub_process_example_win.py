# -*- coding: utf-8 -*-

"""
@File    : 01-sub_process_example_win.py
@Time    : 2021/6/14 12:30
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio


async def main():
    # 创建子进程，执行系统命令dir
    p = await asyncio.create_subprocess_shell('dir')
    # 等待子进程执行完毕
    await p.wait()


asyncio.run(main())
