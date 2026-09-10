#!/usr/bin/env python3

class Book:
    """Represents a book with a title and a page count."""

    def __init__(self, title, page_count):
        # title and page_count are required — no defaults, so the caller
        # must supply both when creating a Book.
        self.title = title
        self._page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        # Only allow integers. If invalid, print a warning instead of
        # raising, and leave the existing value unchanged.
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")