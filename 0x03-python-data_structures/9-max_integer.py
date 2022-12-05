#!/usr/bin/python3

def max_integer(my_list=[]):
    largest = None
    if mylist == []:
        return None
    else:
        for num in my_list:
            if largest == None or num > largest:
                largest = num
