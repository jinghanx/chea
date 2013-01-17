#! /usr/bin/env python
import sys
from tree_generate import get_tree
max_num = -sys.maxint
def f(r):
    global max_num
    if not r:
        return 0
    left = f(r.left)
    right = f(r.right)
    max_num = max(r.value+max(left,right,left+right,0), max_num)
    return r.value + max(left,right,0)
r = get_tree([3,9,20,'#','#',15,7])
f(r)
print max_num
