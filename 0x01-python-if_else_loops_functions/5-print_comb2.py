#!/usr/bin/python3
for num in range(100):
    num_str = str(num)
    if len(num_str) < 2:
        print("0{0}, ".format(num), end="")
    else:
        print("{0}, ".format(num), end="")
