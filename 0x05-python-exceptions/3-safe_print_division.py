#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        i = a/b
        return i
    except ZeroDivisionError:
        i =  None
        return i
    finally:
        print("Inside result: {}".format(i))
