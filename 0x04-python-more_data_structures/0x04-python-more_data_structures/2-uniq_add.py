#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    new_list = list(new_list)
    sumall = 0
    for i in new_list:
        sumall += i

    return sumall


mylist = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(mylist)
print("Result: {:d}".format(result))
