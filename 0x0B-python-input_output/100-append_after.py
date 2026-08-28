#!/usr/bin/python3
"""Append after"""


def append_after(filename="", search_string="", new_string=""):
    """Append after"""

    update_lines = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            update_lines.append(line)
            if search_string in line:
                update_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(update_lines)
