#!/usr/bin/env python3
"""
The code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The code is nearly identical to wait_n except task_wait_random
    is being called.
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*tasks))
