# -*- coding: utf-8 -*-

"""
@File    : aiofile.py
@Time    : 2021/6/14 9:19
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 文件异步IO库
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

    def __init__(self, coroutine):
        # 封装协程
        self._coroutine = coroutine
        # 封装阻塞型IO对象
        self._blocked_file_io = None

    async def __aenter__(self):
        self._blocked_file_io = await self._coroutine
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
        self._blocked_file_io = None

    def __getattr__(self, name) -> AsyncFunWrapper:
        return AsyncFunWrapper(
            getattr(
                self._blocked_file_io,
                name,
            )
        )


# 异步方式打开文件
def async_open(*args) -> AIOWrapper:
    return AIOWrapper(
        asyncio.get_running_loop().run_in_executor(
            None,
            open,
            *args,
        )
    )

