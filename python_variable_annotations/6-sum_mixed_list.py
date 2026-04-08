#!/usr/bin/env python3
"""
This module defines a function `sum_mixed_list` that takes a list of integers
and floats as an argument and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of floats and integers as a float."""
    return sum(mxd_lst)
