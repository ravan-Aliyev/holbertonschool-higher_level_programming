#!/usr/bin/python3
"""5-text_indentation.py, tests/5-text_indentation.txt"""


def text_indentation(text):
    """print a string with newlines after each '.' '?' and ':'.
    text (str): the string to parse and print.

    See tests/5-text_indentation.txt for test cases.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for i in range(len(text)):
        if not text[i] == '.' and not text[i] == '?' and not text[i] == ':':
            print(text[i], end="")
        else:
            print("{}\n".format(text[i]))