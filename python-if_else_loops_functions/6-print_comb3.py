#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            k = str(i) + str(j)
            h = int(k)
            if k != "89":
                print("{}".format(h), end=", ")
            else:
                print("{}".format(h), end=" ")
