#!/usr/bin/python3

"""
This module defines a class
MyInt that inherits from int class
"""


class MyInt(int):
    """
    Invert int operators == and !=
    """

    def __eq__(self, value):
        """
        overrride == operator with
        != behaviour
        """
        return self.real != value

    def __ne__(self, value):
        """
        override != operator
        with == behaviour
        """
        return self.real == value
