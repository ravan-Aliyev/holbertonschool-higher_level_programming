#!/usr/bin/python3
"""Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__value_dimansion(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__value_dimansion(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__value_dimansion(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__value_dimansion(value, "y")
        self.__y = value

    def __value_dimansion(self, value, name):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer.")
        if (name[0] == 'x' or name[0] == 'y') and value < 0:
            raise ValueError(f"{name} must be >= 0.")
        elif (name[0] != 'x' and name[0] != 'y') and value <= 0:
            raise ValueError(f"{name} must be > 0.")
