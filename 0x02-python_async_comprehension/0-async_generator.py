#!/usr/bin/env python3
"""
a python module to define an async generator.
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float]:
    """
    coroutine will loop 10 times, each time asynchronously wait 1 second, 
    then yield a random number between 0 and 10. Use the random module.
    """
    for l in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
