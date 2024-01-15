#!/usr/bin/env python3
""" contains coroutine async_comprehension """
import asyncio
import random
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ coroutine that collects 10 random numbers using an async comprehensing
        Returns:
            10 random numbers
    """
    return [i async for i in async_generator()]
