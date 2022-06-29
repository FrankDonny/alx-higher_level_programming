#!/usr/bin/python3
def printMixChar():
    for i in range(-122, -96):
        i = i * -1
        print("{:c}".format(i if (i % 2 == 0) else (i - 32)), end='')


printMixChar()
