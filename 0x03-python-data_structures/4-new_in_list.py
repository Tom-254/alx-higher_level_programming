#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)
    mynewlist = my_list[:]
    if not (idx > length - 1 or  idx < 0):
        mynewlist[idx] = element
    return mynewlist

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
