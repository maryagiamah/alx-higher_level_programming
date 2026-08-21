#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        sys.stderr.write(f"Exception: {ex.args[0]}\n")
        return False
