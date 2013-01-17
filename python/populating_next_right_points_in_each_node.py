#! /usr/bin/env python
def f(r):
    if not r:
        return
    if r.left:
        r.left.next = r.right
    if r.right:
        r.right.next = r.next.left if r.next.left else None
    f(r.left)
    f(r.right)
