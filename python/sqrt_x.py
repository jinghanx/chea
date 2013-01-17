#! /usr/bin/env python
def f(n):
    begin = 0
    end = n
    while 1:
        mid = (begin+end)/2
        if mid*mid==n or (mid*mid<n and (mid+1)*(mid+1)>n):
            return mid
        elif mid*mid<n:
            begin=mid+1
        else:
            end=mid-1
print f(1372)
