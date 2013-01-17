#! /usr/bin/env python
def f(l):
    if not l:
        return
    prev = None
    index = 0
    for i in range(len(l)):
        if l[i] != prev:
            l[index] = l[i]
            index +=1
        prev = l[index]
    return index
l = [1, 1, 2]
print f(l)
print l
