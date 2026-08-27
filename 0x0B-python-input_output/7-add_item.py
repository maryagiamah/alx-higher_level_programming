#!/usr/bin/python3
"""Add obj items to file"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
from Pathlib import Path
import sys
import json


def add_item():
    """Add item to file"""

    objs = sys.argv[1:]
    filename = sys.argv[0]
    try:
        ob = load_from_json_file(filename)
    except:
        Path.(filename).touch()

    
     save_to_json_file(objs, filename)
  