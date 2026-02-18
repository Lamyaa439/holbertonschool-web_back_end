#!/usr/bin/env python3
# 9-element_length.py
"""
This module have Annotate function's
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    
    """
    return [(i, len(i)) for i in lst]
