#!/usr/bin/env python3
"""async generator module"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine loops 10 times
    it returns a generator that yields a random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
