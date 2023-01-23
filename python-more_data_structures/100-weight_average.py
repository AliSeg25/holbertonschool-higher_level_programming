#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    return sum([x[0] * x[1] for x in my_list]) / sum([x[1] for x in my_list])
print(weight_average([(1, 2), (2, 1), (3, 10), (4, 2)]))