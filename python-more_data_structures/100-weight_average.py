#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    
    total = [sum(x) for x in my_list]
    len = [len(x) for x in my_list]

    return sum(total) / sum(len)
