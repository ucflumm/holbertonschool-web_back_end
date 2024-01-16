#!/usr/bin/env python3
""" contains server class """
import csv
import math
from typing import List, Dict, Union, Any
from functools import reduce


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
            pass

    def index_range(page: int, page_size: int) -> tuple:
        """ returns a tuple of size two containing a start index and an end index
            corresponding to the range of indexes to return in a list for those
            particular pagination parameters
            The page number is 1-indexed
            Returns:
                tuple of start and end indexes
        """
        return ((page - 1) * page_size, page * page_size)
    
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ gets page from dataset
            Args:
                page: page number
                page_size: number of items per page
            Returns:
                list of items
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = Server.index_range(page, page_size)
        return self.dataset()[start:end]
    