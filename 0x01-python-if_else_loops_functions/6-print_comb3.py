#!/usr/bin/python3

for i in range(0, 10):
    for l in range(i + 1, 10):
        if i == 8 and l == 9:
            print("{}{}".format(i, l))
        else:
            print("{}{}".format(i, l), end=", ")
