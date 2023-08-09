#!/usr/bin/env python3
"""
multiple coroutines module
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    wait_n takes in an integer argument (n)
    runs wait_random for n times (default 10)
    returns a list of delays
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    Array = [await task for task in asyncio.as_completed(tasks)]

    return Array
