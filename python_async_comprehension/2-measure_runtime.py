#!/usr/bin/env python3
"""
Create a coroutine called measure_runtime should measure
the total runtime and return it.
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel using asyncio.gather.
    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()
    return end_time - start_time
