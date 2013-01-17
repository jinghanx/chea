# /usr/bin/env python
from treenode import treenode
# [3,9,20,#,#,15,7]
def get_tree(l):
    if not l:
        return
    root = treenode(l[0])
    s = []
    s.append(root)
    index = 1
    while index < len(l):
        next_s = []
        for it in s:
            if l[index] != '#':
                it.left = treenode(l[index])
                next_s.append(it.left)
                index += 1
            else:
                index += 1
            if index >= len(l):
                break
            if l[index] != '#':
                it.right = treenode(l[index])
                next_s.append(it.right)
                index += 1
            else:
                index += 1
            if index >= len(l):
                break
        s = next_s
    return root
