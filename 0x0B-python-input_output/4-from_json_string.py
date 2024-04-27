#!/usr/bin/python3
"""
    this function returns an object (python data structure)
    represented by a JSON string
"""
import json



def from_json_string(json_string):
    """
    this function returns an object (python data structure)
    represented by a JSON string
    """
    return json.loads(json_string)
