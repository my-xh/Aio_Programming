# -*- coding: utf-8 -*-

"""
@File    : 02-decode_sub_process_out.py
@Time    : 2021/6/14 12:36
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio


async def main():
    p = await asyncio.create_subprocess_shell(
        'dir',
        # 将子进程的标准输出重定向到子进程管道
        stdout=asyncio.subprocess.PIPE,
    )
    # 与子进程通信，等待子进程执行结束，并获得子进程的输出信息
    stdout, stderr = await p.communicate()
    # 将获得的信息以gbk的编码方式解码后输出
    print(stdout.decode('gbk'))


asyncio.run(main())
