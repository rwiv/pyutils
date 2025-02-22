import asyncio
from typing import Callable


async def wait_for_func(fn: Callable[[], bool], interval=100, timeout=10000):
    elapsed = 0
    while elapsed < timeout:
        if fn():
            return
        await asyncio.sleep(interval / 1000)
        elapsed += interval
    raise TimeoutError("Condition not met within timeout")
