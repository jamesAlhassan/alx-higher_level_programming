#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_of_args = len(sys.argv) - 1
    if num_of_args == 0:
        print(0)
    for ind in range(1, num_of_args + 1):
        count = 0
        args = int(sys.argv[ind])
        count += args
