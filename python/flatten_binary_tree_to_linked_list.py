#! /usr/bin/env python
from treenode import treenode
from tree_generate import get_tree
from binary_tree_level_order_travelsal import f as print_tree
def f(r):
    if not r:
        return
    s = []
    s.append(r)
    prev = None
    while s:
        n = s.pop()
        if prev:
            prev.right = n
        prev = n
        if n.right:
            s.append(n.right)
        if n.left:
            s.append(n.left)
        n.left=None
    return r
r = get_tree([5,0,-4,-1,-6,-9,'#',7,'#',1,3,'#',0,'#',9,'#','#',6,0,'#',-7,'#','#','#','#','#','#',-4,'#',1,'#','#',-4])
r = f(r)
print_tree(r)
