#!/usr/bin/python3
import random
import asyncio


async def wait_random(max_delay: float = 10.0) -> float:
    """Wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (float): The maximum delay in seconds (default is 10.0).

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
