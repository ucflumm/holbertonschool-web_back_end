#!/usr/bin/env python3
"""Type-annotated function element_length"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Type-annotated function element_length that takes a list
    of strings and returns a list of tuples as a result"""
    return [(i, len(i)) for i in lst]
