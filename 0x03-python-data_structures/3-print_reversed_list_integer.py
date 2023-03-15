#!/bin/usr/python3

def print_reversed_list_integer(my_list=[]):
    my_list = sorted(my_list, None, True)
    [print("{:d}".format(x)) for x in my_list if x==int(x)]
