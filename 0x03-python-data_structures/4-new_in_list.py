#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        new_list = []
        for i in my_list:
            new_list.append(i)
        for j in new_list:
            if j == new_list[idx]:
                del new_list[idx]
                new_list.insert(idx, element)
        return new_list
