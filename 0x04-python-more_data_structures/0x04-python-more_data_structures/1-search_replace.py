#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return
    newlist = my_list.copy()
    for i in range(0, len(newlist)):
        if newlist[i] == search:
            newlist[i] = replace
    return newlist


mylist = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(mylist, 2, 89)

print(new_list)
print(mylist)
