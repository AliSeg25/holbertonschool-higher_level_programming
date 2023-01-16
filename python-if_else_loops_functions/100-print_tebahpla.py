#!/usr/bin/python3
maj = False
for i in range(122, 96, -1):
    lettre = chr(i)
    if maj:
        lettre = lettre.upper()
    print(lettre, end='')
    maj = not maj
