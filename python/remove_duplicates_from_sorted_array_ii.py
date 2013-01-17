#! /usr/bin/env python
def f(l):
    if not l:
        return
    prev = None
    cnt = 0
    index = 0
    for i in range(len(l)):
        if l[i] != prev:
            l[index] = l[i]
            index += 1
            cnt = 0
            prev = l[i]
        else:
            if not cnt:
                l[index] = l[i]
                index += 1
                cnt = 1
    return index
l = [1,1,1,2,2,3]
print f(l)
print l
