#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_a = len(list(tuple_a))
    length_b = len(list(tuple_b))
    if not tuple_a:
        tuple_a = list(tuple_a) + [0, 0]
    elif not tuple_b:
        tuple_b = list(tuple_b) + [0, 0]
    elif length_a < 2:
        tuple_a = list(tuple_a) + [0]
    elif length_b < 2:
        tuple_b = list(tuple_b) + [0]
    elif len(tuple_a) > 2 or len(tuple_b) > 2:
        tuple_a = tuple_a[0:2]
        tuple_b = tuple_b[0:2]
    else:
        tuple_a = list((tuple_a[0], tuple_a[1]))
        tuple_b = list((tuple_b[0], tuple_b[1]))

    m1 = tuple_a[0] + tuple_b[0]
    m2 = tuple_a[1] + tuple_b[1]
    new_list = [m1, m2]
    new_tuple1 = tuple(new_list)
    return new_tuple1
