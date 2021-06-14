# -*- coding: utf-8 -*-

"""
@File    : _aiofile.py
@Time    : 2021/6/14 0:07
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 文件异步IO库（旧版）
"""
import asyncio


class AsyncFunWrapper:

    def __init__(self, blocked_func):
        # 封装阻塞型IO函数
        self._blocked_func = blocked_func

    def __call__(self, *args):
        return asyncio.get_running_loop().run_in_executor(
            None,
            self._blocked_func,
            *args,
        )


class AIOWrapper:

    def __init__(self, blocked_file_io):
        # 封装阻塞型IO对象
        self._blocked_file_io = blocked_file_io

    def __getattribute__(self, name) -> AsyncFunWrapper:
        return AsyncFunWrapper(
            getattr(
                super().__getattribute__('_blocked_file_io'),
                name,
            )
        )


# 异步方式打开文件
async def async_open(*args) -> AIOWrapper:
    return AIOWrapper(
        await asyncio.get_running_loop().run_in_executor(
            None,
            open,
            *args,
        )
    )
