#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Find area of square"""
        return self.__size ** 2

    @property
    def size(self):
        """Get the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("{:{}}".format("", self.__position[0]), end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
