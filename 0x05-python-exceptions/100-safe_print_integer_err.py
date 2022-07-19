#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        if isinstance(value, str):
            print("Exception: Unknown format code 'd' ", file=sys.stderr, end="")
            print("for object of type 'str'", file=sys.stderr)
            return False
        else:
            print("{:d}".format(value))
            return True
    except Exception:
        print("Exception: Unknown format code 'd' ", file=sys.stderr, end="")
        print("for object of type 'str'", file=sys.stderr)
        return False
