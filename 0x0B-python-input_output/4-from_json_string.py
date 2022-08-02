#!/usr/bin/python3
"""from_json_str module"""
import json


def from_json_string(my_str):
    """convert python str to json obj"""
    new = json.loads(my_str)
    return new
