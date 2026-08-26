#!/usr/bin/python3
"""Add attribute"""


def add_attribute(obj, attr, val):
    """Add atttr if not existing"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, val)
