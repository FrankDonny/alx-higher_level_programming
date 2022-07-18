#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    try:
        if len(my_list_1) != len(my_list_2):
            print("out of range")
        else:
            for i in range(0, len(my_list_1)):
                if not isinstance(my_list_1[i] or my_list_2[i], int or float):
                    print("Wrong Type")
                elif my_list_1[i] / my_list_2[i]:
                    list_length.append(my_list_1[i] / my_list_2[i])
                else:
                    list_length.append(0)
        return list_length
    except (ZeroDivisionError, IndexError):
        print("division by 0")
    finally:
        print([li for li in list_length])
