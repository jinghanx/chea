#! /usr/bin/env python
def f(l):
    if not l:
        return [1]
    carry = 1
    for i in range(len(l)-1,-1,-1):
        ans = l[i]+carry
        l[i] = ans%10
        carry = ans/10
    if carry:
        l.insert(0,1)
    print l
f([3,2,5,9])
