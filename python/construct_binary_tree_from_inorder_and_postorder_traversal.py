#! /usr/bin/env python
from binary_tree_level_order_travelsal import f as print_tree
from treenode import treenode
def find_irootindex(ino, posto, ileft, iright, prootindex):
    for i in range(ileft, iright + 1):
        if ino[i] == posto[prootindex]:
            return i
    return

def f(ino, posto, ileft, iright, pleft, pright):
    if ileft > iright:
        return
    prootindex = pright
    irootindex = find_irootindex(ino, posto, ileft, iright, prootindex)
    root = treenode(ino[irootindex])
    left_length = irootindex - ileft
    right_length = iright - irootindex
    root.left = f(ino, posto, ileft, irootindex-1, pleft, pleft+left_length-1)
    root.right = f(ino, posto, irootindex+1, iright, pright-right_length, pright-1)
    return root

root = f([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3, 5, 4, 2, 8, 9, 7, 6], 0, 8, 0, 8)
print_tree(root)
