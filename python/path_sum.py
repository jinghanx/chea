#! /usr/bin/env python
from tree_generate import get_tree
def f(r,target):
    if not r and not target:
        return True
    elif not r:
        return False

    return f(r.left, target-r.value) or f(r.right, target-r.value)
r = get_tree([1,-2,-3,1,3,-2,'#',-1])
print f(r,-1)
