#!/usr/bin/python3

def number_keys(a_dictionary):
    num_of_keys = 0
    list_of_keys = list(a_dictionary)
    for num in list_of_keys:
        num_of_keys += 1
    return num_of_keys
