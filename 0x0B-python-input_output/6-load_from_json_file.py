#!/usr/bin/python3
"""
a function that creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """
    a function that creates an object from a json file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
