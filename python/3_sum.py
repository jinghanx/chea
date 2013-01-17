#! /usr/bin/env python
def f(l):
    if not l:
        return
    l.sort()
    res = []
    prev_i = None
    for i in range(len(l) - 2):
        if prev_i == l[i]:
            prev_i = l[i]
            continue
        left = i + 1
        right = len(l) - 1
        prev_left = None
        prev_right = None
        while left < right:
            if prev_left == l[left]:
                prev_left = l[left]
                left += 1
                continue
            if prev_right == l[right]:
                prev_right = l[right]
                right -= 1
                continue
            if l[left] + l[right] + l[i] == 0:
                res.append([l[i], l[left], l[right]])
                prev_left = l[left]
                prev_right = l[right]
                left += 1
                right -= 1
            elif l[left] + l[right] + l[i] < 0:
                prev_left = l[left]
                left += 1
            else:
                prev_right = l[right]
                right -= 1
        prev_i = l[i]
    for it in res:
        print it
f([-1,0,0,1,1,2,-1,4])
