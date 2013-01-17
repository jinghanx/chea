#! /usr/bin/env python
def f(r):
    if not r:
        return 0
    return max(f(r.left), f(r.right)) + 1

# post-order iterative version 1
def f(r):
    if not r:
        return
    s = []
    s.append(r)
    prev = None
    mx = 0
    while s:
        node = s[-1]
        if not prev or prev.left == node or prev.right == node:
            if node.left:
                s.append(node.left)
            elif node.right:
                s.append(node.right)
        elif node.left = prev:
            if node.right:
                s.append(node.right)
        else:
            s.pop()
        prev = node
        mx = max(mx, len(s))
    return mx
def f(r):
    if not r:
        return
    s = []
    s.append(r)
    previous = None
    while s:
        n = s[-1]
        if not previous or previous.left == n or previous.right == n:
            if n.left:
                s.push(n.left)
            if n.right:
                s.push(n.right)
        elif previous == n.left:
            if n.right:
                s.push(n.right)
        else:
            s.pop()
            print n.value
        previous = n

