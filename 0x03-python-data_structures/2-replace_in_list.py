#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if not (idx > length - 1 or idx < 0):
        my_list[idx] = element
    return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 2
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
