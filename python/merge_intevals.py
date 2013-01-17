#! /usr/bin/env python
def f(s1):
    res = []
    head = s1[0][0]
    tail = s1[0][1]
    for it in s1:
        if tail < it[0]:
            res.append([head, tail])
            head = it[0]
            tail = it[1]
        else:
            tail = max([tail, it[1]])
    res.append([head,tail])
    return res
print f([[1,3],[2,6],[8,10],[15,18]])
