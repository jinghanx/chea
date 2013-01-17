#! /usr/bin/env python
from tree_generate import get_tree
def f(r):
    if not r:
        return
    s = []
    s.append(r)
    while 1:
        next_s = []
        for it in s:
            print it.value,
            if it.left:
                next_s.append(it.left)
            if it.right:
                next_s.append(it.right)
        s = next_s
        if not s:
            break
        print

#r = get_tree([3,9,20,'#','#',15,7])
#f(r)
