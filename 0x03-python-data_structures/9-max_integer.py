#!/usr/bin/python3

def max_integer(my_list=[]):
    b = 0
    if len(my_list) == 0:
        return None
    for i in range(0, len(my_list)):
        if my_list[i] > b:
            b = my_list[i]
    return b
