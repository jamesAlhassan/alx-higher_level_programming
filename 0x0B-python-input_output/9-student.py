#!/usr/bin/python3
"""A module that defines a class 'Student'"""


class Student:
    """A class 'student'"""

    def __init__(self, first_name, last_name, age):
        """Object Initialization a new"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the Student"""
        return self.__dict__
