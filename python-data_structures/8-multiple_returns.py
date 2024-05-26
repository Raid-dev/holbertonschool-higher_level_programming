#!/usr/bin/python3
def multiple_returns(sentence):
    first_letter = None if len(sentence) == 0 else sentence[0]
    tuple = (len(sentence), first_letter)
    return tuple
