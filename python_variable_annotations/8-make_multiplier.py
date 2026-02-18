#!/usr/bin/env python3
# 8-make_multiplier.py
"""
This module have a type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a
    float by multiplier
    """
    def multiply(n: float) -> float:
        """Multiplies n by the multiplier."""
        return n * multiplier
    return multiply
