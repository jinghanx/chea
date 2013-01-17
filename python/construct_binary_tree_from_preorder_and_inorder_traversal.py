#! /usr/bin/env python
from treenode import treenode
from binary_tree_level_order_travelsal import f as print_tree
def find_iroot(ino, preo, ileft, iright, proot):
    for i in range(ileft, iright+1):
        if ino[i] == preo[proot]:
            return i
def f(ino, preo, ileft, iright, pleft, pright):
    if ileft > iright:
        return
    proot = pleft
    iroot = find_iroot(ino, preo, ileft, iright, proot)
    left_length = iroot - ileft
    right_length = iright - iroot
    root = treenode(ino[iroot])
    root.left = f(ino, preo, ileft, iroot-1, pleft+1, pleft+left_length)
    root.right = f(ino, preo, iroot+1, iright, pright-right_length+1, pright)
    return root
root = f([1,2,3,4],[4,2,1,3], 0, 3, 0, 3)
print_tree(root)
