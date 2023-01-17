#!/usr/bin/python3

"""A class that inherits from 'Rectangle' """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ A child class of Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String reprsentation of the class object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
