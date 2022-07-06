#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return
    newlist = my_list.copy()
    for i in range(0, len(newlist)):
        if newlist[i] == search:
            newlist[i] = replace
         else:
            continue
    return newlist
