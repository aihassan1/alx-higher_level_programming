#!/usr/bin/python3


if __name__ == "__main__":
    import sys

    args_num = len(sys.argv)

    if args_num == 1:
        print("0 arguments.")

    elif args_num == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))

    else:
        print("{} arguments:".format(args_num - 1))

        for i in range(1, args_num):
            print("{}: {}".format(i, sys.argv[i]))
