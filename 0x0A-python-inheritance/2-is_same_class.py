#!/usr/bin/python3
"""
This module contains the function is_same_class that test if obj is an object of type a_class
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class as a_class, otherwise false"""
    return (type(obj) == a_class)
