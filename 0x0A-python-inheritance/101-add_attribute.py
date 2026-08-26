#!/usr/bin/python3
"""Add attribute"""


def add_attribute(obj, attr, val):
    """Add atttr if not existing"""

    if hasattr(obj, attr):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, Val)
