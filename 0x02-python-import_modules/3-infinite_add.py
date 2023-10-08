#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    import sys

    args_num = len(sys.argv) - 1

    result = 0

    if args_num == 0:
        print("0")

    else:
        for i in range(1, args_num + 1):
            result = result + int(argv[i])

        print(result)
