#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if not (idx > length - 1 or idx < 0):
        del my_list[idx]
    return my_list


if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)
