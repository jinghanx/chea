#! /usr/bin/env python
from tree_generate import get_tree
def f(r):
    if not r:
        return
    res = []
    s = []
    s.append(r)
    res.append(s)
    flag = 0
    while 1:
        next_s = []
        for it in s:
            if it.left:
                next_s.append(it.left)
            if it.right:
                next_s.append(it.right)
        if not next_s:
            break
        s = next_s
        if flag:
            res.append(s)
        else:
            res.append(list(reversed(s)))
        flag = 1 - flag
    return res

r = get_tree([3,9,20,'#','#',15,7])
res = f(r)
for it in res:
    for it2 in it:
        print it2.value,
    print

