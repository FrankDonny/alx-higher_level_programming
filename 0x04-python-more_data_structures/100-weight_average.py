#!/usr/bin/python3
def weight_average(my_list=[]):
    if bool(my_list) == 0:
        return 0

    new_list = []
    newlist1 = []
    sumall = 0
    sumall1 = 0
    for mem in my_list:
        mem = list(mem)
        newlist1.append(mem[1])
        total = mem[0] * mem[1]
        new_list.append(total)
    for j in newlist1:
        sumall1 += j
    for i in new_list:
        sumall += i
    result = sumall/sumall1
    return result
