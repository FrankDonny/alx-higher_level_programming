#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx > length:
        return my_list
    else:
        for i in my_list:
            if i == my_list[idx]:

                del my_list[idx]
                my_list.insert(idx, element)
    return my_list
