#!/usr/bin/python3
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int | float]]) -> float:
    """Returns the sum of a list of floats and integers as a float."""
    return sum(mxd_lst)
