#!/usr/bin/env python3
"""
Module that provides a helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for the
    given pagination parameters.
    """
    start_index = (page - 1) page_size
    end_index = page * page_size
    return (start_index, end_index)