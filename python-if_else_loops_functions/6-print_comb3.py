#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            k = str(i) + str(j)
            if k != "89":
                print("{}".format(k), end=", ")
            else:
                print("{}".format(k), end="")
