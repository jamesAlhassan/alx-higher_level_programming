#!/usr/bin/python3
for letter in range(ord("a"), ord("z") + 1):
    if letter == ord("q") or letter == ord("e"):
        continue
    else:
        print("{0:c}".format(letter), end="")
