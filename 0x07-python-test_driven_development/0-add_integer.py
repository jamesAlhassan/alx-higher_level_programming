#!/usr/bin/python3
"""
A module with one function 'add_interger' that adds two integers

"""

def add_integer(a, b=98):
    """
    Return the sum of two integers or floats as integers
    Args:
        a: first argument
        b: second argument
    Return:
        Sum of 'a' and 'b'
    Raise:
        TypeError: If either 'a' or 'b' not int or float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be na integer")
    return (int(a) + int(b))

