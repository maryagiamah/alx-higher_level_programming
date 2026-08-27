#!/usr/bin/python3
""" Student Class"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Init Method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To json"""

        if isinstance(attrs, list) and all(isinstance(b, str) for b in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """"Reload fromm JSON"""

        for k, v in json.items():
            setattr(self, k, v)
