#!/usr/bin/python3i
def search_replace(my_list, search, replace):
    copy = my_list[:]
    index = copy.index(search)
    copy[index] = replace
    return copy
