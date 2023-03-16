#!/usr/bin/python3

if __name__=="__main__":
	import sys
	count = len(sys.argv)
	if (count==2):
		print("{:d}: argument".format(count-1))
	else:
		print("{:d}: arguments".format(count-1))
	for i in range(count-1):
		print("{:d}: {:s}".format(i+1, sys.argv[i]))
