#! /usr/bin/env python
import sys
def f(l):
    mx = -sys.maxint
    print mx
    prev = 0
    for it in l:
        mx = max(mx, prev+it)
        prev = 0 if prev+it<0 else prev+it
    return mx
print f([-2,-3,-1])
