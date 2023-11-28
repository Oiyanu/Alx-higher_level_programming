#!/usr/bin/python3
for z in range(97, 123):
    if z in [101, 113]:
        continue
    print("{}".format(chr(z)), end='')
