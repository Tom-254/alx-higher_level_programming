#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    listed = list(a_dictionary.items())

    for key, val in listed[:]:
        if value == val:
            del a_dictionary[key]

    return a_dictionary


if __name__ == "__main__":
    print_sorted_dictionary = \
        __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
