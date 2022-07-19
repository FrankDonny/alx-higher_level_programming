#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        if isinstance(value, str):
            print("Exception: Unknown format code", file=sys.stderr)
            return False
        else:
            print("{:d}".format(value))
            return True
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
