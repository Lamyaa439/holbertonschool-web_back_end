#!/usr/bin/env python3
"""
Module implementing deletion-resilient hypermedia pagination.
"""
import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize Server with empty dataset and indexed dataset caches.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.
        Skips the header row and returns all data rows.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Build and cache a dictionary mapping each row's original index
        to its data.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient page of data starting at a given index.
        """
        dataset = self.indexed_dataset()

        assert index is not None and 0 <= index < len(dataset), \
            "index must be a valid integer within the dataset range"

        data = []
        current_index = index

        while len(data) < page_size:
            if current_index in dataset:
                data.append(dataset[current_index])
            current_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': current_index
        }
