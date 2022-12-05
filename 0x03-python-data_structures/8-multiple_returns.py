#!/usr/bin/python3

def multiple_returns(sentence):
    t = ()
    if sentence == "":
        return None
    else:
        length = len(sentence)
        first_char = sentence[0]
    tupl = (length, first_char)
    return tupl
