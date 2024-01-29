#!/usr/bin/python3i
def search_replace(my_list, search, replace):
    if my_list != []:
        copy = my_list.copy()
        index = copy.index(search)
        copy[index] = replace
        return copy
