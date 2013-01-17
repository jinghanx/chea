#! /usr/bin/env python

class node:
    def __init__(self, value):
        self.value = value;
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.value)

def find(ino, n):
    for i in range(len(ino)):
        if ino[i] == n:
            return i

def f(ino, left_ino, right_ino, preo, left_preo, right_preo):
    if left_ino > right_ino:
        return
    root = node(preo[left_preo])
    root_ino = find(ino, preo[left_preo])
    root.left = f(ino, left_ino, root_ino-1, preo, left_preo+1, root_ino-left_ino+left_preo)
    root.right = f(ino, root_ino+1, right_ino, preo, root_ino-left_ino+left_preo+1, right_preo)
    return root

n = f([1,2,3,4],0,3,[1,2,4,3],0,3)
res = []
q = []
q.append(n)
res.append(q)
while 1:
    q_tmp = []
    for it in q:
        if it.left:
            q_tmp.append(it.left)
        if it.right:
            q_tmp.append(it.right)
    q = q_tmp
    if not q:
        break;
    res.append(q)
for it in res:
    for it2 in it:
        print it2
