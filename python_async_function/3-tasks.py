#!/usr/bin/env python3
"""Function that takes in an integer max_delay and returns a asyncio.Task.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
