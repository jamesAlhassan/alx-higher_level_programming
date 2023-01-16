#!/usr/bin/python3
"""A child class of Base """

from models.base import Base


class Rectangle(Base):
    """A class than inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Object Instantiation method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the value of width like an attribute"""
        return self.__width

    @property
    def height(self):
        """Get the value of height"""
        return self.__height

    @property
    def x(self):
        """ Get the value of x"""
        return self.__x

    @property
    def (self):
        """Get the value of y like an attribute"""
        return self.__y
