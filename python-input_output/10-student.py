#!/usr/bin/python3
"""
    Modul that returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object
"""


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """initialisation method """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Function that returns the JSON representation
            of an instance of a Class
        """
        if not hasattr(self, '__dict__'):
            return None  # Not an instance of a class with attributes

        json_dict = {}
        for attr_name, attr_value in self.__dict__.items():
            if isinstance(attr_value, (list, dict, str, int, bool)):
                json_dict[attr_name] = attr_value

        if isinstance(attrs, list):
            f_dict = {k: v for k, v in json_dict.items() if k in attrs}
            return f_dict

        return json_dict
