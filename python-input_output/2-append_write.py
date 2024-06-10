#!/usr/bin/python3
"""
    Modul that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
