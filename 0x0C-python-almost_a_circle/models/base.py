#!/usr/bin/python3
"""Base class for all classes"""


class Base:
    """ Base class for all other class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """objects Instantiation method"""
        if id not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
