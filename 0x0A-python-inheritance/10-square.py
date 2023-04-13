#!/usr/bin/python3
"""
Defines a rectangle subclass: Square"""


class Square(Rectangle):
    """
    Represents a square
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        slef.__size = size
