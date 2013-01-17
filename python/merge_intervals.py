#! /usr/bin/env python
import operator
def f(l):
    if not l:
        return
    l.sort(key=operator.itemgetter(0))
    res = []
    start = l[0][0]
    end = l[0][1]
    for i in range(1, len(l)):
        if end < l[i][0]:
            res.append([start,end])
            start = l[i][0]
            end = l[i][1]
        elif end < l[i][1]:
            end = l[i][1]
    res.append([start,end])
    return res
res = f([])
for it in res:
    print it
