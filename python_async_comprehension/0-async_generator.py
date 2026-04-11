#!/usr/bin/env python3
"""
Create coroutine will loop 10 times, each time asynchronously
wait 1 second and yield a random number between 0 and 10 inclusive.
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """Asynchronous generator that yields random numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
