#!/usr/bin/python3
"""
    Basic serialization module that adds the functionality to serialize
    a Python dictionary to a JSON file and deserialize the JSON file to
    recreate the Python Dictionary
"""


def serialize_and_save_to_file(data, filename):
    """
        This function serializes data and saves it to file as JSON data.

        data:     A Python Dictionary with data
        filename: The filename of the output JSON file. If the output file
                  already exists it should be replaced.
    """
    import json
    import os

    if os.path.exists(filename):
        os.remove(filename)

    with open(filename, 'w', encoding='utf-8') as file:
        j_str = json.dumps(data)
        file.write(j_str)


def load_and_deserialize(filename):
    """
        This function returns a Python Dictionary with the deseialized JSON
        data from the file.

        filename: The filename of the output JSON file.
    """
    import json

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
