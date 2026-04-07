#!/usr/bin/python3
from typing import Iterator, Sequence, List, Tuple


def element_length(lst: Iterator[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
