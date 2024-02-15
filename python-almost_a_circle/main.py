#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))


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