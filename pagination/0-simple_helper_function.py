#!/usr/bin/env python3
"""
contains function index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters
        The page number is 1-indexed
        Returns:
            tuple of start and end indexes
    """
    return ((page - 1) * page_size, page * page_size)
