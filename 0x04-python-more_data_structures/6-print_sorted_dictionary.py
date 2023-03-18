#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    result = {}
    for x in sorted(list(a_dictionary.keys()), reversed=False):
        result[x] = a_dictionary[x]
    return result
