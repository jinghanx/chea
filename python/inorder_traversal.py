#! /usr/bin/env python
from tree_generate import get_tree
def f(r):
    if not r:
        return
    s = []
    s.append(r)
    prev = None
    while s:
        n = s[-1]
        if not prev or prev.left == n or prev.right == n:
            if n.left:
                s.append(n.left)
            else:
                print n.value
                s.pop()
                if n.right:
                    s.append(n.right)
            prev = n
        else:
            print n.value
            s.pop()
            if n.right:
                s.append(n.right)
            prev = n
r = get_tree([1,2,5,3,4,'#',6])
f(r)
