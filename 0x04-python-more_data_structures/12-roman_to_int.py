#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    values = {"I": 1,
              "V": 5,
              "X": 10,
              "L": 50,
              "C": 100,
              "D": 500,
              "M": 1000,
              }

    total = 0
    count = 0
    length = len(roman_string)
    while count < length:
        rom_val1 = values[roman_string[count]]
        if count + 1 < length:
            rom_val2 = values[roman_string[count + 1]]
            if rom_val1 >= rom_val2:
                total = total + rom_val1
                count = count + 1
            else:
                total = total - rom_val1
                count = count + 1
        else:
            total = total + rom_val1
            count = count + 1
    return total


if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
