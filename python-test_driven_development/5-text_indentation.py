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

    tex = []

    for i in text:
        tex.append(i)
   
    for i in range(len(tex)):
        if tex[i] in tab:
            print(tex[i], end="\n\n")
        else:
            print(tex[i], end="")

text_indentation("Holberton. School? How are you:    John")