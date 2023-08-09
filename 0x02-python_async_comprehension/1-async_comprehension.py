#!/usr/bin/env python3
"""async comprehensions module"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine that collects 10 numbers using async_generator
    it returns a list of 10 random numbers from async_generator
    """
    numbers = [i async for i in async_generator()]
    return numbers
