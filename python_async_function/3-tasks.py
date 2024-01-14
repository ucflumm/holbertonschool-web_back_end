#!/usr/bin/env python3
"""
Regular function task_wait_random that takes an integer max_delay
and returns a asyncio.Task.
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Regular function task_wait_random that takes an integer max_delay
        and returns a asyncio.Task.
    """
    return asyncio.create_task(task_wait_random(max_delay))
