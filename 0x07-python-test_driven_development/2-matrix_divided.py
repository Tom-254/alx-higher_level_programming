"""This module holds the function matrix_divided which takes in a matrix
and divides each element by 3
"""


def matrix_divided(matrix, div):
    """Returns a new matrix that has been divided by div
    Args:
        matrix (list[list]): a list of lists
        div (int): the number to divide by
    Return:
        list[list]:a new matrix
    """

    row_check = 0
    if not any(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of\
                        integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of\
                        integers/floats")
    if matrix[0] is not None:
        row_check = len(matrix[0])
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of\
                            integers/floats")
        for num in row:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError("matrix must be a matrix (list of lists) of\
                                integers/floats")
        if len(row) != row_check:
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
