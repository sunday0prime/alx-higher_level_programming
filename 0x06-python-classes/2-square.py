#!/usr/bin/python3
"""A module that defines a square"""

class Square:
	"""A class that defines a square"""

	def __init__(self, size=0):
		"""Initializes a square instance
			Args:
				size: size
			Raises:
				TypeError: type check fails
				ValueError: value check fails
		"""
		if not type(size) is int:
			raise TypeError("size must be an integer")
		if (size < 0):
			raise ValueError("size must be >= 0")
		self.__size = int(size)
