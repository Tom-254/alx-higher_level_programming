#!/usr/bin/python3

def element_at(my_list, idx):
    length = len(my_list)
    if not (idx > length - 1 or idx < 0):
        return my_list[idx]
    return None


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = -1
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
