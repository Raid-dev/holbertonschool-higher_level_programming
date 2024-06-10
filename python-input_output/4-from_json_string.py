#!/usr/bin/python3
"""
    Modul that returns  an object (Python data structure)
    represented by a JSON string
"""


def from_json_string(my_str):
    """Function that returns an object represented by a JSON"""

    import json
    return json.loads(my_str)
