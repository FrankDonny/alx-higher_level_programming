#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence != "":
        for i in sentence:
            a = sentence[0]
            return length, a
    else:
        return length, None
