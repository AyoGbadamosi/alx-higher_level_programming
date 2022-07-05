#!/usr/bin/python3
"""
This module contains Save Object to a file task
"""

import json


def save_to_json_file(my_obj, filename):
    ''' Writes JSON representation of object to file '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
