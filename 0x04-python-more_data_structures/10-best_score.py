#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value."""
    if a_dictionary is None:
        return None
    maxval = 0
    maxkey = None
    for k, v in a_dictionary.items():
        if v > maxval:
            maxval = v
            maxval = k
    return maxkey
