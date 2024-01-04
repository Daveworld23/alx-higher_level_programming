#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    fron sys import argv
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    ops = argv[2]
    b = int(argv[3])
    if ops == '+':
        print("{a} {ops} {b} = {add(a, b)}")
    elif ops == '-':
        print("{a} {ops} {b} = {sub(a, b)}")
    elif ops == '*':
        print("{a} {ops} {b} = {mul(a, b)}")
    elif ops == '/':
        print("{a} {ops} {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
