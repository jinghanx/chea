#! /usr/bin/env python
def f(l, n):
    if not l:
        return
    index = 0
    for i in range(len(l)):
        if l[i] != n:
            l[index] = l[i]
            index += 1
    return l[:index]
print f([1,2,3,4], 4)
