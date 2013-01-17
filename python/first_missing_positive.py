#! /usr/bin/env python
def swap(l,i):
    tmp = l[l[i]-1]
    l[l[i]-1] = l[i]
    l[i]=tmp

def f(l):
    if not l:
        return 1
    length = len(l)
    for i in range(len(l)):
        while l[i] > 0 and l[i]<=length:
            if l[i] != i+1:
                swap(l, i)
            else:
                break
    for i in range(len(l)):
        if l[i] <= 0 or l[i]>length:
            return i+1
print f([3,4,-1,1])
