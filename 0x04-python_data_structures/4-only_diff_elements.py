#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    result = {}
    for x in set_1:
        if not x in set_2:
            result[len(result)] = x
    return result
