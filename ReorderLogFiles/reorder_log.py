#!/usr/bin/env python

from collections import deque

input = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
res = deque()

for items in input:
    if items.split(" ")[1].isdigit():
        res.append(items)
    else:
        res.appendleft(items)

print res
