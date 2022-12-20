#!/usr/bin/python3

"""Class with a private attribute 'size'"""


class Square:
    """a class 'Square' with a private attribute 'size' """
    def __init__(self, size):
        self._size = size


square = Square(size)
