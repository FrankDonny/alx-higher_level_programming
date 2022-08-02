#!/usr/bin/python3
import json
"""to_json_string module"""


def to_json_string(my_obj):
    """convert json str to python obj"""
    new = json.dumps(my_obj)
    return new
