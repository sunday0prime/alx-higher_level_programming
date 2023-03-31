#!/usr/bin/python3

class Square:
	def __init__(self, size):
		if not type(size) is int:
			raise TypeError("size must be an integer")
		if (size < 0):
			raise ValueError("size must be >= 0")
		self.__size = size

	@property
	def size(self):
		return (self.__size)

	@size.setter
	def size(self, value):
		if not type(value) is int:
			raise TypeError("size must be an integer")
		if (value < 0):
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		return (self.__size**2)

	def my_print(self):
		print("{}".format((("#"*self.__size)+"\n")*self.__size))
