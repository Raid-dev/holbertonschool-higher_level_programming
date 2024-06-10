#!/usr/bin/python3
"""
    Modul that returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object
"""


def class_to_json(obj):
    """
        Function that returns the JSON representation
        of an instance of a Class
    """
    if not hasattr(obj, '__dict__'):
        return None  # Not an instance of a class with attributes

    json_dict = {}
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            json_dict[attr_name] = attr_value

    return json_dict
