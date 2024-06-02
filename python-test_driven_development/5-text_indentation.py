#!/usr/bin/python3
""" Text Indentation module """

def text_indentation(text):
    """ Modifies text """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{}\n\n".format(text[i], end=""))
        else:
            print("{}" .format(text[i]), end="")
