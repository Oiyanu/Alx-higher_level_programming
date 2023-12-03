#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    for z in range(len(my_list)):
        if z == idx:
            my_list[z:z+1] = []
            return my_list
