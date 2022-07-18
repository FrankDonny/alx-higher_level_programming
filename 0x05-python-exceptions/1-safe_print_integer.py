#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if isinstance(value, str):
            return False
        else:
            print("{:d}".format(value))
            return True
    except Exception:
        return False
