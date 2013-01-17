#! /usr/bin/env python
import sys
def f(r):
    if not r:
        return
    s = []
    s.append(r)
    prev = None
    mx = sys.maint
    while s:
        n = s[-1]
        if not prev or prev.left == n or prev.right == n:
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)
        elif prev == n.left:
            if n.right:
                s.append(r.right)
        else:
            s.pop()
        prev = n
        mx = min(mx, len(s))
