#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = str(number)
if number < 0:
    last_num = -(int(num_str[-1]))
else:
    last_num = int(num_str[-1])

if last_num > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
elif last_num < 6 and not 0:
    print(f"Last digit of {number} is {last_num} and is less than 6 not 0")
