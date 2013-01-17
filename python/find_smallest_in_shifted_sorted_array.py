#! /usr/bin/env python
def f(l, left, right):
    if left == right:
        return l[left]
    if left == right - 1:
        return min(l[left], l[right])
    mid = (left + right)/2
    if l[mid] < l[left] and l[mid] < l[right]:
        return l[mid]
    else:
        if l[mid] < l[right]:
            return f(l, left, mid-1)
        else:
            return f(l, mid+1, right)
print f([3,2], 0, 1)
