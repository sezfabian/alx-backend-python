#!/usr/bin/env python3
""" Async gather module"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    returns runtime after executing comprehension 4 times in parallel
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop = time.perf_counter()
    return stop - start
