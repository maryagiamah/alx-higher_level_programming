#!/usr/bin/python3
"""Save obj to file"""
import json


def save_to_json_file(my_obj, filename):
    """Serialisation to file"""

    with open(filename, "w",
              encoding="utf-8") as f:
        json.dump(my_obj, f)
