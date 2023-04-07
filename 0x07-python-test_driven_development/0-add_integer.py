#!/usr/bin/python3

"""
This module contains a function that adds to numbers and returns the result.
"""

def add_integer(a, b=98):
    """
    add_integer is a function that adds 2 numbers
    >>>add_integer(2, 5)
    7
    >>>add_integer(2, -5)
    -3
    >>>add_integer(2)
    100
    >>>add_integer('six', 1)
    TypeError()
    """

    if not type(a) in (int, float):
        raise TypeError("a must be an integer")
    if not type(b) in (int, float):
        raise TypeError("b must be an integer")
    return int(a + b)
