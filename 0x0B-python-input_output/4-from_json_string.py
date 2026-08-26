#!/usr/bin/python3
"""From JSON string to object"""
import json


def from_json_string(my_str):
    """Deserialise"""

    return json.loads(my_str)
