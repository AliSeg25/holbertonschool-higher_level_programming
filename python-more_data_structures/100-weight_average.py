#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    
    total = sum([sum(x) for x in my_list])
    long = sum([len(x) for x in my_list])

    return total / len
