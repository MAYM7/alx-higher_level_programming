#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    dev = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            dev.append(True)
        else:
            dev.append(False)
    return (dev)
