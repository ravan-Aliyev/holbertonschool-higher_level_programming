#!/usr/bin/python3
""" 9-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

    #         @property
    # def width(self):
    #     return self.__width

    # @width.setter
    # def width(self, value):
    #     self.__value_dimansion(value, "width")
    #     self.__width = value

    # @property
    # def height(self):
    #     return self.__height

    # @height.setter
    # def height(self, value):
    #     self.__value_dimansion(value, "height")
    #     self.__height = value

    # @property
    # def x(self):
    #     return self.__x

    # @x.setter
    # def x(self, value):
    #     self.__value_dimansion(value, "x")
    #     self.__x = value

    # @property
    # def y(self):
    #     return self.__y

    # @y.setter
    # def y(self, value):
    #     self.__value_dimansion(value, "y")
    #     self.__y = value

    # def __value_dimansion(self, value, name):
    #     """Check validation"""
    #     if type(value) != int:
    #         raise TypeError(f"{name} must be an integer.")
    #     if (name[0] == 'x' or name[0] == 'y') and value < 0:
    #         raise ValueError(f"{name} must be >= 0.")
    #     elif (name[0] != 'x' and name[0] != 'y') and value <= 0:
    #         raise ValueError(f"{name} must be > 0.")