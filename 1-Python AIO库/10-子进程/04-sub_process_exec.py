# -*- coding: utf-8 -*-

"""
@File    : 04-sub_process_exec.py
@Time    : 2021/6/14 12:51
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""
import asyncio


async def main():
    p = await asyncio.create_subprocess_exec(
        r'C:\Program Files\ImageMagick-7.0.10-Q16-HDRI\ffmpeg.exe',
        # 将子进程的标准输出重定向到子进程管道
        stdout=asyncio.subprocess.PIPE,
        # 将子进程的标准错误输出重定向到子进程管道
        stderr=asyncio.subprocess.PIPE,
    )
    # 循环读取直到数据结尾
    while not p.stderr.at_eof():
        # 从子进程的标准错误输出管道中读取一行数据
        line = await p.stderr.readline()
        if line:
            print(line.decode('gbk'), end='')


asyncio.run(main())
