#!/usr/bin/python3
"""a class 'Square' with a private and public instance attribute"""


class Square:
    """ class 'Square' definition"""

    def __init__(self, size=0):
        """instance initialization
        Arg: size
        Raise:
            TypeError: if size not integer
            ValueError: if size less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__self = size

    def area(self):
        """
        method 'area' definition
        Return : square of size
        """
        return (self.__size ** 2)
