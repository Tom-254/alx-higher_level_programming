#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in range(len(matrix)):
        inner_len = len(matrix[row])
        for col in range(inner_len):
            print("{:d}".format(matrix[row][col]),
                  end="" if inner_len - 1 == col else " ")
        print()


if __name__ == "__main__":

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
