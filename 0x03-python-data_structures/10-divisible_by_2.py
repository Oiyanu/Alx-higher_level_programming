#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    temp_list = my_list.copy()
    for z in range(len(my_list)):
        if my_list[z] % 2 == 0:
            temp_list[z] = True
        else:
            temp_list[z] = False
    return temp_list
