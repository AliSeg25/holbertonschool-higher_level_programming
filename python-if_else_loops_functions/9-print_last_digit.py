#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        modulo_du_posetif = (number*-1) % 10
        print(modulo_du_posetif)
        return modulo_du_posetif
    else:
        print(number % 10)
