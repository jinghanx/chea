#! /usr/bin/env python
def s(a, b, tail_a):
    index = len(a) - 1
    tail_b = len(b)-1
    while tail_b >= 0 and tail_a >= 0:
        if a[tail_a] > b[tail_b]:
            a[index] = a[tail_a]
            tail_a -= 1
        else:
            a[index] = b[tail_b]
            tail_b -= 1
        index -= 1
    while tail_b >= 0:
        a[index] = b[tail_b]
        index -= 1
        tail_b -= 1
    return a
def f(a1, a2):
    if not a1 and not a2:
        return
    elif not a1:
        return a2
    elif not a2:
        return a1
    res = []
    i1 = 0
    i2 = 0
    while i1!=len(a1) and i2!=len(a2):
        if a1[i1] < a2[i2]:
            res.append(a1[i1])
            i1+=1
        else:
            res.append(a2[i2])
            i2+=1
    while i1!=len(a1):
        res.append(a1[i1])
        i1+=1
    while i2!=len(a2):
        res.append(a2[i2])
        i2+=1
    print res
f([1,3,5,7,8],[2,4,6,9,10])
