#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator """
    for _ in range(10):
        # async wait 1 second
        await asyncio.sleep(1)
        # yield random number between 0 and 10
        yield random.uniform(0, 10)
