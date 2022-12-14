#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    real_number = 0
    for elem in range(x):
        try:
            print("{:d}".format(my_list[elem]), end="")
            real_number += 1
        except (TypeError, ValueError):
            pass
    print()
    return real_number


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
