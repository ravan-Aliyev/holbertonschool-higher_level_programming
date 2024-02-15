#!/usr/bin/python3
"""Base class"""
import json
import os


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

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
