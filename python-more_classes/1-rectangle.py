#!/usr/bin/python3
"""Create new class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Init function of class"

            Args:
                width (int): The width of the new rectangle.
                height (int): The height of rectangle.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self):
        """Getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter of width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
