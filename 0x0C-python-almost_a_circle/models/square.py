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

    @property
    def size(self):
        """ Gets the value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """ sets the value of size"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.__height = value
