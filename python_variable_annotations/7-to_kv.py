#!/usr/bin/env python3
"""
This module defines a function `to_kv` that takes a string and an integer or
float as arguments and returns a tuple of the string and the square
of the number.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of the key and the square of the value."""
    return (k, v ** 2)
