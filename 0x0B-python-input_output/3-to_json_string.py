#!/usr/bin/python3
""" A modlue containing  to_json_string fun """
import json


def to_json_string(my_obj):
    """ returns json repr of my-obj """
    return json.dumps(my_obj)
