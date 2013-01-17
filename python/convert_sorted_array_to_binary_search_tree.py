#! /usr/bin/env python
from treenode import treenode
from binary_tree_level_order_travelsal import f as print_tree
def f(l, left, right):
    if left > right:
        return
    mid = (left + right) / 2
    root = treenode(l[mid])
    root.left = f(l, left, mid-1)
    root.right = f(l, mid+1, right)
    return root
l = [9,12,14,17,19,23,50,54,67,72,76]
root = f(l, 0, len(l)-1)
print_tree(root)
