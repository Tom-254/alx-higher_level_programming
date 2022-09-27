#!/usr/bin/python3

def pascal_triangle(n):
    p_list = []
    for line in range(1, n + 1):
        C = 1
        row = []
        for i in range(1, line + 1):
            row.append(C)
            C = int(C * (line - i) / i)
        p_list.append(row)
    return p_list
