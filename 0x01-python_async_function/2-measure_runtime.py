#!/usr/bin/env python3
"""
Measure runtime module
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    measures the total execution time for wait_n(n, max_delay)
    returns total_time / n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
