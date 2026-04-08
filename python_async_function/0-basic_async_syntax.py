#!/usr/bin/env python3
"""
Function that takes an integer argument (max_delay, with a default value of 10)
and returns a float.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds and return it.
    Args:
        max_delay (int): The maximum delay in seconds (default is 10).
    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
