#!/usr/bin/python3
"""Print text indented module"""


def text_indentation(text):
    """
    prints text followed by 2 new lines after ".", "?", or ":"
    @text: the text to be printed
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    tab = [".", "?", ":"]
    words = text.split()

    tabtexte = []

    for i in text:
        tabtexte.append(i)

    for i in tabtexte:
        if i in tab:
            print(i, end="\n\n")
        else:
            print(i, end="")
