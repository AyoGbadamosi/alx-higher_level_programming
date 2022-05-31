#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number >= 0):
    j = number % 10
    if (j > 5):
        print(f"Last digit of {number} is {j} and is greater than 5")
    elif (j == 0):
        print(f"Last digit of {number} is {j} and is 0")
    else:
        print(f"Last digit of {number} is {j} and is less than 6 and not 0")
else:
    j = -number % 10
    print(f"Last digit of {number} is {-j} and is less than 6 and not 0")
