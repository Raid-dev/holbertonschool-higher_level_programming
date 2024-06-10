#!/usr/bin/python3
"""
    Modul that creates an Object from a JSON file
"""


def load_from_json_file(filename):
    """Function that creates an Object from a JSON file"""

    import json

    with open(filename, 'r', encoding="utf-8") as f:
        json_string = f.read()
        return json.loads(json_string)
