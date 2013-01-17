#! /usr/bin/env python
import sys
def f(l):
    left = []
    right = []
    mx = -sys.maxint
    low = sys.maxint
    high = -sys.maxint

    # left
    for it in l:
        left.append(max(mx,it-low))
        low = min(it, low)
        mx = max(mx, it-low)

    mx = -sys.maxint

    left[0] = 0
    for i in range(len(l)-1, -1, -1):
        mx = max(mx, high - l[i])
        high = max(high, l[i])
        right.append(mx)

    right.reverse()
    right[-1] = 0
    print l
    print left
    print right

    res = -sys.maxint
    for i in range(len(l)):
        res = max(res, left[i]+right[i])
    print res


f([1,2,4,2,5,7,2,4,9,0])
