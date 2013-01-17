#! /usr/bin/env python
def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

def f(l):
    index1 = 0
    index3 = len(l)-1
    i = 0
    while i<=index3:
        if l[i] == 1:
            swap(l,index1, i)
            index1+=1
            i+=1
        elif l[i] == 3:
            swap(l, index3, i)
            index3-=1
        else:
            i+=1
    return l
print f([1,3,3])
