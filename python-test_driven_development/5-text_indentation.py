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

    for i in range(len(words)):
        word = words[i]
        if word[-1] in tab:
            print(word, end="\n\n")
        else:
            print(word, end=" ")