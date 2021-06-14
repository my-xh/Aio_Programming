# -*- coding: utf-8 -*-

"""
@File    : 03-read_sub_process_until_end.py
@Time    : 2021/6/14 12:44
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
    # 循环读取直到数据结尾
    while not p.stdout.at_eof():
        # 从子进程的标准输出管道中读取一行数据
        line = await p.stdout.readline()
        if line:
            # 将获得的信息以gbk的编码方式解码后输出
            print(line.decode('gbk'), end='')


asyncio.run(main())
