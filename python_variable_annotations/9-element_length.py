#!/usr/bin/env python3
"""
This module defines a function `element_length` that takes an iterator of
sequences as an argument and returns a list of tuples, where each tuple
contains a sequence from the iterator and its length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains a sequence from the
    iterator and its length.
    """
    return [(i, len(i)) for i in lst]
