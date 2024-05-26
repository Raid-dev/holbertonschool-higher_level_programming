#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = list(tuple_a) + [0] * (2 - len(tuple_a))
    tuple_b = list(tuple_b) + [0] * (2 - len(tuple_b))
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
