#! /usr/bin/env python
from tree_generate import get_tree
import copy
def f(r, target):
    if not r:
        return False
    s = []
    s.append(r)
    prev = None
    res = []
    while s:
        n = s[-1]
        if not prev or prev.left==n or prev.right==n:
            target -= n.value
            if n.left:
                s.append(n.left)
            elif n.right:
                s.append(n.right)
            elif not target:
                res.append(copy.deepcopy(s))
        elif prev == n.left:
            if n.right:
                s.append(n.right)
        else:
            s.pop()
            target+=n.value
        prev = n
    for it in res:
        for it2 in it:
            print it2.value,
        print
r = get_tree([5,4,8,11,'#',13,4,7,2,'#','#',5,1])
f(r,21)
