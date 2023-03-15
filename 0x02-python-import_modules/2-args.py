#!/usr/bin/python3

if __name__="__main__":
	import sys

	if len(sys.argv):
		count = len(sys.argv)
		if count==1:
			print("{} argument".format(count-1))
		else:
			print("{} arguments:".format(count-1))
		for i in range(count-1):
			print("{}: {}".format(i+1, sys.argv[i]))
