#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle("2", "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))


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