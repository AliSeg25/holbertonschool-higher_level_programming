#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    somme_ponderee = 0
    poids_total = 0
    for i, j in my_list:
        somme_ponderee += i * j
        poids_total += j
    return somme_ponderee / poids_total
