#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = str(number)
last_digit = int(number_string[-1])
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif number < 0 and number != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")

