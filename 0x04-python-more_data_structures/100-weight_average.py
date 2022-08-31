#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        score_total = 0
        weighted_sum = 0
        for tup in my_list:
            score_total += (tup[0] * tup[1])
            weighted_sum += tup[1]
        return (score_total / weighted_sum)
    return 0

if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
