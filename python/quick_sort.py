#! /usr/bin/env python
import random
def f(l, left, right):
    if left>right:
        return
    pivot = random.randint(left, right)
    index = left
    i = right-1
    swap(l,right,pivot)
    while i>=index:
        if l[i] < l[pivot]:
            swap(l, i, index)
            index+=1
            continue
        i-=1
    swap(l,index,right)
    f(l,left,index-1)
    f(l,index+1, right)
    return

def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

l = [0]
f(l, 0,0)
print l
