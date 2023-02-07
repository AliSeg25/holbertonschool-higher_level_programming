#!/usr/bin/python3
"""Function append_write"""


def append_write(filename="", text=""):
    with open(filename, "a") as fichier:
        fichier.write(text)
        return text