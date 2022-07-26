#!/usr/bin/python3
"""
This module contains the text_indentation function
"""


def text_indentation(text):
    """
    Description: This function indents the text passed at position
    where '.', '?' and ':' are found
    if text is not a string, raise TypeError
    """

    if not isinstance(text, str):
        raise TypeError("text must be a text")
    li = ['.', '?', ':']
    for i in text[::1]:
        if i in li:
            text = text[:text.index(i) + 1] + '<>' + text[text.index(i) + 1:]
        else:
            text = text[:]
    print(text)
