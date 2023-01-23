#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nv_list = my_list[:]
    if idx < 0 or idx > len(nv_list)-1:
        return nv_list
    else:
        nv_list[idx] = element
        return nv_list
