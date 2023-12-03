#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = [tuple_a[k] if k < len(tuple_a) else 0 for k in range(2)]
    list_b = [tuple_b[k] if k < len(tuple_b) else 0 for k in range(2)]

    sum0 = list_a[0] + list_b[0]
    sum1 = list_a[1] + list_b[1]
    new_t = (sum0, sum1)

    return (new_t)
