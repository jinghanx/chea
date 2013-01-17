#! /usr/bin/env python
def f(l, left, right, target):
    if not l:
        return -1
    if left > right:
        return -1
    mid = left + (right - left) / 2
    if l[mid] == target:
        return mid
    else:
        if l[mid] < l[right]:
            if l[mid] < target:
                if target > l[right]:
                    return f(l, left, mid-1, target)
                else:
                    return f(l, mid+1, right, target)
            else:
                return f(l, left, mid-1, target)
        else:
            if l[mid] < target:
                return f(l, mid+1, right,target)
            else:
                if target <= l[right]:
                    return f(l, mid+1, right, target)
                else:
                    return f(l, left, mid-1, target)
print f([9,0,4,8], 0, 3,0)

