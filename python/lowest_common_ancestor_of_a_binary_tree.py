#! /usr/bin/env python
# Top down
def f(r, p, q):
    if not r:
        return
    if r == p or r == q:
        return
    matchleft = helper(r.left, p, q)
    matchright = helper(r.right, p, q)
    if matchleft and matchright:
        return r
    elif matchleft:
        return f(r.left, p, q)
    else:
        return f(r.right, p, q)
