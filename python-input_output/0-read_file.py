#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read data from filename"""
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
    print(read_data)
