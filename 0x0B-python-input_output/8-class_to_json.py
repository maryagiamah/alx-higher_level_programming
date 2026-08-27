#!/usr/bin/python3
""" class_to_json """
import json


def class_to_json(obj):
    """Convert class to json"""

    return json.loads(obj.__dict__)
