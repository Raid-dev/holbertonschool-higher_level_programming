#!/usr/bin/python3
""" Square Printer module """


def print_square(size):
    """ Prints square with # """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size > 0:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
