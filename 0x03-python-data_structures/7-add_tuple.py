#!/usr/bin/python3
def add_tuple(tuple_aa=(), tuple_bb=()):
    length_a = len(list(tuple_aa)) - 1
    length_b = len(list(tuple_bb)) - 1
    if not tuple_aa:
        tuple_aa = list(tuple_aa) + [0, 0]
    elif not tuple_bb:
        tuple_bb = list(tuple_bb) + [0, 0]
    elif length_a < 2:
        tuple_aa = list(tuple_aa) + [0]
    elif length_b < 2:
        tuple_bb = list(tuple_bb) + [0]
    elif len(tuple_aa) > 2 or len(tuple_bb) > 2:
        tuple_aa = tuple_aa[0:2]
        tuple_bb = tuple_bb[0:2]

    m1 = tuple_aa[0] + tuple_bb[0]
    m2 = tuple_aa[1] + tuple_bb[1]
    new_list = [m1, m2]
    new_tuple1 = tuple(new_list)
    return new_tuple1
