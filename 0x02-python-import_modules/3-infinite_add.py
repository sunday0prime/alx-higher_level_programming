#!/usr/bin/python3

if __name__ = "__main__":
    import sys

    sum = 0
    for x in sys.argv:
        sum += int(x)
    print(sum)
