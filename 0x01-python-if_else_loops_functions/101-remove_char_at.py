#!/usr/bin/python3

def remove_char_at(str, n):
    i = 0

    while str[i] != '\0':
        if i != n and i < n:
            str2[i] = str[i]
        elif i != n and i > n:
            str2[i - 1] = str[i]
        i = i + 1
    return str2
