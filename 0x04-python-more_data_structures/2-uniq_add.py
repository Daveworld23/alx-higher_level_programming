#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    d = 0
    for i in uniq_list:
        d += i
    return (d)
