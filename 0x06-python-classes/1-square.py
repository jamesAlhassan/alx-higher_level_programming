#!/usr/bin/python3

"""Class with a private attribute 'size'"""


class Square:
    """a class 'Square' with a private attribute 'size' """
    def __init__(self, size):
        """ instance initialization
        Arg: size 
        """
        self.__size = size
