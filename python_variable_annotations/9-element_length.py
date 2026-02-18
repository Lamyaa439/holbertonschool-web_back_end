#!/usr/bin/env python3
# 9-element_length.py
"""
This module have Annotate function's
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate the below function's parameters and return values with
    the appropriate types
    """
    return [(i, len(i)) for i in lst]
