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

    @classmethod
    def save_to_file(cls, list_objs):
        arr = []
        file_path = f"{cls.__name__}.json"
        for cl in list_objs:
            class_dict = cl.to_dictionary()
            arr.append(class_dict)

        if os.path.exists(file_path):
            with open(f"{cls.__name__}.json", "a") as f:
                f.write(cls.to_json_string(arr))
        else:
            with open(f"{cls.__name__}.json", "w") as f:
                f.write(cls.to_json_string(arr))
