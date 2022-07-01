from calculator_1 import add, sub
import sys

length = len(sys.argv)
a = sys.argv[1]
b = sys.argv[3]
if length != 4:
    print("Usage:./100 - my_calculator.py < a > < operator > < b >")
elif length < 1:
    pass
else:
    for operator in ['+', '-', '*', '/']:
        if operator == '+':
            print("{} {} {} = {}".format(a, operator, b, add(int(a), int(b))))
            exit(0)
        elif operator == '-':
            print("{} {} {} = {}".format(a, operator, b, sub(int(a), int(b))))
            exit(0)
