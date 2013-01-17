#! /usr/bin/env python
def f(x,n):
    res = 1.0
    while n:
        if n&1:
            res *=x
        x *=x
        n = n>>1
    return res
print f(2,10)
