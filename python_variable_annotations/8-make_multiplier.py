#!/usr/bin/env python3
"""
This module defines a function `make_multiplier` that takes a float as an
argument and returns a function that multiplies a float by the multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
