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

    @static_method
    def to_json_string(list_dictionaries):
        """JSON String"""
        if not list_dictionaries:
            return []

        return json.dumps(list_dictionaries)