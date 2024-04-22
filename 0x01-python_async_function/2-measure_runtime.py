#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime
    """
    start = time()

    asyncio.run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
