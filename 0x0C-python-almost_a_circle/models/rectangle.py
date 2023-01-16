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

    def __str__(self):
        """String representation of the class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

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
    def y(self):
        """Get the value of y like an attribute"""
        return self.__y

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @y.setter
    def y(self, value):
        """ sets the value of y"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')

        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """ returns the area of the reactangle 'Rectangle'"""
        return (self.__width * self.__height)

    def display(self):
        """Displays '#' shape of the rectangle"""
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args):
        """ assigns an argument to each attribute"""
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "id":
                    if b is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = b
                elif a == "width":
                    self.width = b
                elif a == "height":
                    self.height = b
                elif a == "x":
                    self.x = b
                elif k == "y":
                    self.y = b
