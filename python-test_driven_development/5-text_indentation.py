#!/usr/bin/python3
"""Print text indented module"""


def text_indentation(text):
    """
    prints text followed by 2 new lines after ".", "?", or ":"
    @text: the text to be printed
    """
    tab = [".", "?", ":"]
    tabtext = text.split()

    for i in range(len(tabtext)):
        text2 = tabtext[i]
        if text2[-1] in tab:
            print(text2)
            print("\n")
        else:
            print(text2, end=" ")
