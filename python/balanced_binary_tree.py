#! /usr/bin/env python
def helper(r):
    if not r:
        return 0
    left = f(r.left)
    right = f(r.right)
    if left == -1:
        return -1
    if right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    else:
        return 1 + max(left, right)
def f(r):
    res = helper(r)
    if res == -1:
        return False
    else:
        return True
def max_height(r):
    if not r:
        return 0
    else:
        return max(max_height(r.left), max_height(r.right))+1
def min_height(r):
    if not r:
        return 0
    else:
        return min(min_height(r.left), min_height(r.right))+1
def f(r):
    if not r:
        return
    mx = max(max_height(r.left), max_height(r.right))
    mi = min(min_height(r.left), min_height(r.right))
    if mx-mi >= 2:
        return False
    return True
