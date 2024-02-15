#!/usr/bin/python3
"""Base class"""
import json
import os
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves JSON str to file"""
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as fd:
            if list_objs is None:
                fd.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                fd.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        clase = {}
        if "size" in dictionary:
            clase = cls(dictionary["size"])
            clase.update(**dictionary)
        else:
            clase = cls(dictionary["width"], dictionary["height"])
            clase.update(**dictionary)
        return clase

    @classmethod
    def load_from_file(cls):
        file_name = f"{cls.__name__}.json"
        data = []
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                dic = cls.from_json_string(f.read())
                data = [cls.create(**a) for a in dic]
        return data

    @staticmethod
    def draw(list_rectangles, list_squares):
        for obj in list_rectangles:
            rectangle = turtle.Turtle()
            rectangle.color("blue")
            rectangle.penup()
            rectangle.goto(obj.x, obj.y)
            rectangle.pendown()
            for _ in range(2):
                rectangle.forward(obj.width)
                rectangle.left(90)
                rectangle.forward(obj.height)
                rectangle.left(90)
        for obj in list_squares:
            square = turtle.Turtle()
            square.color("red")
            square.penup()
            square.goto(obj.x, obj.y)
            square.pendown()
            for _ in range(4):
                square.forward(obj.size)
                square.left(90)

        turtle.done()
