#!/usr/bin/python3
"""A module that defines a square"""

class Square:
	"""A class that represents a square"""
	def __init__(self, size=0):
		"""Inititilises this square instance
			Args:
				size: the size
			Raises:
				TypeError: type check fails
				ValueError: value check fails
		"""
		self.__size = size
