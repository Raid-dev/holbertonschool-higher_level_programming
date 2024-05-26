#!/usr/bin/python3
"""Module containing the definition of the Square class."""

class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize the Square with a given size."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of square with given size."""
        return self.__size**2
