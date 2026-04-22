#!/usr/bin/env python3
""" 0-simple_helper_function.py """


def index_range(page, page_size):
    """Return a tuple of start and end indexes for pagination."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
