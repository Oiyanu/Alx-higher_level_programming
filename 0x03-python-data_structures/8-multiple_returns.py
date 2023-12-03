#!/usr/bin/python3
def multiple_returns(sentence):
    string_len = len(sentence)
    if string_len == 0:
        first_char = None
    else:
        first_char = sentence[0]
    new_t = (string_len, first_char)
    return new_t
