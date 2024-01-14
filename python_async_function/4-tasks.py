#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Take the code from wait_n and alter it into a new function task_wait_n.
        The code is nearly identical to wait_n except task_wait_random is being
        called.
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    completed_tasks = await asyncio.gather(*tasks)
    return sorted(completed_tasks)
