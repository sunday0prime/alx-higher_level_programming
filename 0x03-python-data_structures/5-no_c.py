#!/usr/bin/python3


def no_c(my_string):
    updated_str = ""
    for i in my_string:
        if i!="c" and i!="C":
            updated_string +=i
    return (updated_str)
