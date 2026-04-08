#!/usr/bin/env python3
"""
This module defines a function `sum_list` that takes a list of floats as an argument
and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats as a float."""
    return sum(input_list)
