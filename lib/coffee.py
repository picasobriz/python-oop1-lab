#!/usr/bin/env python3

class Coffee:
    """Represents a cup of coffee with a size and a price."""

    VALID_SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size in self.VALID_SIZES:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Note: uses a curly apostrophe (’) to match the exact string
        # the test asserts against — a straight apostrophe (') will fail.
        print("This coffee is great, here’s a tip!")
        self.price += 1