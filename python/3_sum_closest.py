#! /usr/bin/env python
import sys

def f(l, target):
    if not l:
        return
    l.sort()
    delta = sys.maxint
    ans = None
    prev = None
    for i in range(len(l) - 2):
        if prev == l[i]:
            prev = l[i]
            continue
        left = i + 1
        right = len(l) - 1
        while left < right:
            curr = l[left] + l[right] + l[i]
            if curr == target:
                ans = curr
                return ans
            elif curr < target:
                if abs(curr - target) < delta:
                    delta = abs(curr-target)
                    ans = curr
                left += 1
            else:
                if abs(curr - target) < delta:
                    delta = abs(curr-target)
                    ans = curr
                right -= 1
        prev = l[i]
    print ans
f([1,2,-1,-4],1)
