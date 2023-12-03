#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list)
    if list_len == 0:
        return None
    max = my_list[0]
    for z in range(list_len):
        if my_list[z] > max:
            max = my_list[z]
    return max
