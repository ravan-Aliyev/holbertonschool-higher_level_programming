#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        self.__width = size
        self.__height = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__width
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self) -> str:
        return f"[Square] ({self.id}) {self.x}/{self.y}\
 - {self.width}"
