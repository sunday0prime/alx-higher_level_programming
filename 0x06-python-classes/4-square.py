#!/usr/bin/python3
"""A module containing a square class"""

class Square:
	"""A class representing a square"""

	def __init__(self, size=0):
		"""Initializes a square"""
		if not type(size) is int:
			raise TypeError("size must be an integer")
		if (size < 0):
			raise ValueError("size must be >= 0")
		self.__size = size

	@property
	def size(self):
		"""Retrives size"""
		return self.__size

	@size.setter
	def size(self, value):
		"""Updates size
		Returns: size
		"""
		if not type(value) is int:
			raise TypeError("size must be an integer")
		if (value < 0):
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		"""Returns: area of square"""
		return (self.__size**2)
