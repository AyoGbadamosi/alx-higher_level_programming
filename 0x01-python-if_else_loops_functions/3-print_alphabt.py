#!/usr/bin/python3
'''program that prints the ASCII alphabet'''

for i in range(97, 123):
    if (chr(i) != 'q' and chr(i) != 'e'):
        print(f"{chr(i)}", end="")
