#! /usr/bin/env python
def f(r):
    prev = r
    s = []
    s.append(r)
    while s:
        cur = s.pop()
        if cur.right:
            s.push(cur.right)
        if cur.left:
            s.push(cur.left)
        if cur != prev:
            prev.left = None
            prev.right = cur
            prev = cur
        else:
            prev.left=None
    return r
