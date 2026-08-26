#!/usr/bin/python3
"""Save obj to file"""


def save_to_json_file(my_obj, filename):
    """Serialisation to file"""

    with open(filename, encoding="utf-8"):
        f.write(json.dump(obj))
