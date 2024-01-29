#!/usr/bin/python3i
def search_replace(my_list, search, replace):
    copy = my_list.copy()
    index = copy.index(search)
    copy[index] = replace
    return copy
