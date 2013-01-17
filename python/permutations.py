#! /usr/bin/env python
from copy import copy
def f(l):
    res = [[]]
    index = 0
    while index!= len(l):
        tmp_res =[]
        for it in res:
            for i in range(len(it)+1):
                it.insert(i, l[index])
                tmp_res.append(copy(it))
                del it[i]
        res = tmp_res
        index+=1
    for it in res:
        print it
f([1,2,3])
