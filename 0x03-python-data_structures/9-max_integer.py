#!/usr/bin/python3

def max_integer(my_list=[]):
    b = 0
    for i in range(0, len(my_list)):
        if my_list[i] > b:
            b = my_list[i]
    return b
