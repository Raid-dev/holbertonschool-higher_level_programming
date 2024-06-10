#!/usr/bin/python3
"""Modul that returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object"""

    import json
    return json.dumps(my_obj)
