#!/usr/bin/env python3
"""
Module that implements simple pagination for a dataset of baby names.
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for the
    given pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the correct page of data from the dataset.
        """
        assert isinstance(page, int) and isinstance(page_size, int), \
            "page and page_size must be integers"
        assert page > 0 and page_size > 0, \
            "page and page_size must be greater than 0"
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return[]
        return dataset[start:end]
    