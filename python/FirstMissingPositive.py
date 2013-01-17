#! /usr/bin/env python

def f(l):
    for i in range(len(l)):
        while l[i]!=i+1:
            if l[i]<=0 or l[i]>len(l):
                break
            tmp = l[l[i]-1]
            l[l[i]-1] = l[i]
            l[i] = tmp
    for i in range(len(l)):
        if l[i]!=i+1:
            return i+1
    return len(l)+1
print f([3,4,-1,1])
