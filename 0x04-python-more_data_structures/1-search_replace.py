#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list."""
    return list(map(lambda e: replace if e == search else e, my_list))
