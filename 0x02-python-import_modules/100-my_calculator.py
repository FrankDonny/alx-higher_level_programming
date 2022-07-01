#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main_":
    length = len(sys.argv)

    for i in range(0, length):
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[i] == sys.argv[0]:
            continue
        elif length != 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
        elif lenght == 3:
            for operator in ["+", "-", "*", "/"]:
                if operator == '+':
                    print("{} {} {} = {}".format(a, operator, b, add(a, b)))
                    #exit(0)
                elif operator == '-':
                    print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
                    #exit(0)
                elif operator == '*':
                    print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
                    #exit(0)
                elif operator == '/':
                    print("{} {} {} = {}".format(a, operator, b, div(a, b)))
                    #exit(0)
                else:
                    print("Unknown operator. Available operators: +, -, * and /")
