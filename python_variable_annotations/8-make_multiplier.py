#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function returns a function
    that multiplies a float by multiplier
    """
    def multiply_by_multiplier(number: float) -> float:
        """This function returns the product of a float and multiplier"""
        return number * multiplier
    return multiply_by_multiplier
