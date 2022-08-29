#!/usr/bin/python3

def multiple_returns(sentence):
    len_str = len(sentence)
    return (len_str, sentence[0] if len_str > 0 else None)


if __name__ == "__main__":

    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
