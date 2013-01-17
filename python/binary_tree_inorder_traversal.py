#! /usr/bin/env python
def f(r):
    if not r:
        return
    s = []
    curr = r
    while not s or not curr:
        if curr:
            s.append(curr.left)
        else:
            s.pop()
