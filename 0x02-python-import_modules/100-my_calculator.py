#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    from calculator_1 import add, div, mul, sub

    args_number = len(argv) - 1
    if args_number != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    valid_oprators = ['+', '-', '/', '*']

    oprator = argv[2]

    if oprator not in valid_oprators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if oprator == '+':
        add_result = add(a, b)
        print("{} + {} = {}".format(a, b, add_result))

    elif oprator == '-':
        sub_result = sub(a, b)
        print("{} - {} = {}".format(a, b, sub_result))

    elif oprator == '*':
        mul_result = mul(a, b)
        print("{} * {} = {}".format(a, b, mul_result))

    else:
        div_result = div(a, b)
        print("{} / {} = {}".format(a, b, div_result))
