#!/usr/bin/python3

"""
A function that prints a square with a specified number of  character #
"""


def print_square(size):
    """
    Prints a square with character #

    Arg:
       size - An integer showing the length of the square

    Raises:
        TypeError: if size is not an integer
        Typerror: if size is a float and less than zero
        ValueError: if size is less than zero
    """
    if size < 0:
        raise ValueError("size must be >= 0")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        for x in range(size):
            print("#", end="")
        print("")
