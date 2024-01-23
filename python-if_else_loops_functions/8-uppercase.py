#!/usr/bin/python3
def uppercase(str):
    str_cpy = ""
    for i in range(len(str)):
        if ord('a') <= ord(str[i]) <= ord('z'):
            str_cpy += chr(ord(str[i]) - 32)
            continue
        str_cpy += str[i]
    print(str_cpy)
