#! /usr/bin/env python
def f(l):
    if not l:
        return 0
    left = 0
    right = len(l)-1
    mx = min(l[left], l[right]) * (right - left )
    while left < right:
        if l[left] < l[right]:
            prev = l[left]
            while l[left] <= prev:
                left += 1
                if left >= len(l):
                    break
        else:
            prev = l[right]
            while l[right] <= prev:
                right -= 1
                if right <= -1:
                    break
        if left >= right:
            break
        mx = max(mx, min(l[left], l[right]) * (right - left))
    return mx
print f([1,1])
