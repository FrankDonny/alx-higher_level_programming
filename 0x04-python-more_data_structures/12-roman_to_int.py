#!/usr/bin/python3
from string import ascii_letters
def roman_to_int(roman_string):
    letters = ascii_letters
    for i in range(0, len(roman_string)):
        if roman_string[i] not in letters:
            return 0
    roman_string = str(roman_string).upper()
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    sumall = 0
    last = "I"
    for letter in roman_string[::-1]:
        if my_dict[letter] < my_dict[last]:
            sumall -= my_dict[letter]
        else:
            sumall += my_dict[letter]
        last = letter
    return sumall
