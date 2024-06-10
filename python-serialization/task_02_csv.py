#!/usr/bin/python3
"""
    reading data from one format (CSV) and converting it into another
    format (JSON) using serialization techniques
"""


def convert_csv_to_json(csv_filename):
    """
        Thi the CSV filename as its parameter and writes the
        JSON data to data.json

        filename: The filename of CSV file.
    """
    import json
    import csv

    try:
        with open(csv_filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

            json_filename = 'data.json'
            with open(json_filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
                return True
    except FileNotFoundError:
        print("File not found.")
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False
