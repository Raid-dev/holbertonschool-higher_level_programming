#!/usr/bin/python3
"""Modul that prints txt file"""


def read_file(filename=""):
    """Function that reads and prints txt file """

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
