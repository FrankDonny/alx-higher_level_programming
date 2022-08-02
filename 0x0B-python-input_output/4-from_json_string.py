#!/usr/bin/python3
import json
"""from_json_str module"""


def from_json_string(my_str):
    """convert python str to json obj"""
    new = json.loads(my_str)
    return new
