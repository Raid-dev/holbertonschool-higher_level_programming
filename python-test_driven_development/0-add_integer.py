#!/usr/bin/python3
""" Integers Addition module"""


def add_integer(a, b=98):
    """ Adds two integers """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b
