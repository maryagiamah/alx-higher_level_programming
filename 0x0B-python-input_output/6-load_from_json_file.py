#!/usr/bin/python3
"""Recover object from file"""
import json


def load_from_json_file(filename):
    """DeSerialisation"""

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
