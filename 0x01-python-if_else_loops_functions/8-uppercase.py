#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            print((ord(letter) - 32))
            letter = chr((ord(letter) - 32))
        print("{}".format(letter), end="")