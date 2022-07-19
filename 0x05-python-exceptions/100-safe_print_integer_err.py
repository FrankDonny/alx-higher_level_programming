#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if isinstance(value, str):
            print("Exception: Unknown format code 'd' ", end="")
            print("for object of type 'str'")
            return False
        else:
            print("{:d}".format(value))
            return True
    except Exception:
        return False
