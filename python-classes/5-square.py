#!/usr/bin/python3
"""Module containing the definition of the Square class."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize the Square with a given size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of square with given size."""
        return self.__size**2

    def my_print(self):
        """Prints the square with # for given size."""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#"*self.size)
