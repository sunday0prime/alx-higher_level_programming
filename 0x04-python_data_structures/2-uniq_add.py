#!/usr/bin/python3

def uniq_add(my_list=[]):
    newlist = []
    for x in my_list:
        if not x in newlist:
            newlist.append(x)
    return sum(newlist)
