#!/usr/bin/python3

for i in range(0, 10):
    for l in range(digit1 + 1, 10):
        if i == 8 and l == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
