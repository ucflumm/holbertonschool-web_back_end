#!/usr/bin/env python3
"""
Measure the runtime with an asynchronous comprehension
"""
import asyncio
import random
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Import wait_random from 0-basic_async_syntax.
        Write a function (do not create an async function, use the regular
        function syntax to do this) task_wait_random that takes an integer
        max_delay and returns a asyncio.Task.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
