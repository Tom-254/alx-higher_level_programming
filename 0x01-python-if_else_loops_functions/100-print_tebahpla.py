#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        print(f"{i - 32:c}", end='')
    else:
        print(f"{i:c}", end='')

