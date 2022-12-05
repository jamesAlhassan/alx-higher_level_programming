#!/usr/bin/python3

def max_integer(my_list=[]):
    largest = None
    for num in my_list:
        if num == None or num > largest:
            largest = num
