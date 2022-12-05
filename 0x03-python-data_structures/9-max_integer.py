#!/usr/bin/python3

def max_integer(my_list=[]):
    largest = None
    if len(my_list) == 0:
        return None
    else:
        for num in my_list:
            if largest == None or num > largest:
                largest = num
    return largest
