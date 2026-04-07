#!/usr/bin/env python3
from typing import Union, Tuple


def to_kv(k: str, v: Union[int | float]) -> Tuple[str, float]:
    """Returns a tuple of the key and the square of the value."""
    return (k, v ** 2)
