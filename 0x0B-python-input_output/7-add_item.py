#!/usr/bin/python3
"""Add obj items to file"""
import sys
import os
from pathlib import Path


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file




objs = sys.argv[1:]
filename = "add_item.json"

try:
    curr_obj = load_from_json_file(filename)
except FileNotFoundError:
    curr_obj = []

    curr_ob.extend(objs)
    save_to_json_file(curr_ob, filename)
