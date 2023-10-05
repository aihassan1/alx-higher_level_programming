#!/usr/bin/python3

i = 122

while i > 97:

    print("{}".format(chr(i)), end='')
    i -= 33

    print("{}".format(chr(i)), end='')
    i += 31
