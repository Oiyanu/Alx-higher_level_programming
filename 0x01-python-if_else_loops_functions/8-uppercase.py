#!/usr/bin/python3
def uppercase(str):
    for z in str:
        temp = z
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(z) - 32)
        print("{}".format(temp), end='')
    print()
