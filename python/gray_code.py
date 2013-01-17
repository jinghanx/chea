#! /usr/bin/env python
import copy
def f(n):
    if not n:
        return []
    res = []
    res.append(0)
    base = 1
    for i in range(n):
        length = len(res)
        for j in range(length-1, -1, -1):
            res.append(res[j]+base)
        base = base<<1
    for it in res:
        print it
f(3)
