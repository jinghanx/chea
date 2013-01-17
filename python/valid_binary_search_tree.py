#! /usr/bin/env python
import treenode

def f(r, mi, mx):
    if not r:
        return True
    if r.val < mi or r.val > mx:
        return False
    return f(r.left, mi, r.val) && r(r.right, r.val, mx)

