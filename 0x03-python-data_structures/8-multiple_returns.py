#!/usr/bin/python3

def multiple_returns(sentence):
    leng = len(sentence)
    first = sentence[0]
    if leng == 0:
        return (0, None)
    else:
        return (leng, first)
