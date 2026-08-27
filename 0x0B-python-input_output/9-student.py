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

        return self.__dict__
