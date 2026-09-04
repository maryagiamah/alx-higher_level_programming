#!/usr/bin/python3
""" Base Class"""
import json


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        '''init Method'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON String"""
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to file"""

        filename = f"{cls.__name__}.json"
        list_dicts = None

        if list_objs:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        x = cls.to_json_string(list_dicts)

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(x)

    def from_json_string(json_string):
        """From JSON string"""
        if not json_string or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create"""
        new_obj = None 
        if cls.__name__ == "Square":
            new_obj = cls(5)
        else:
            new_obj = cls(5, 6)

        new_obj.update(**dictionary)
        return new_obj
