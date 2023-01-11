#!/usr/bin/python3
"""A module that defines a text file-reading function"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
