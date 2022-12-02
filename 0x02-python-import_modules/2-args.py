#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_of_args = len(sys.argv) - 1

    if num_of_args == 0:
        print("0 arguments.")
    elif num_of_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_of_args))
    for ind in range(num_of_args):
        print("{}: {}".format(ind + 1, sys.argv[ind + 1]))
