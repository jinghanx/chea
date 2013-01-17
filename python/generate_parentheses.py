#! /usr/bin/env python
def f(n):
    return helper(n,n)
def helper(left, right):
    if not left and not right:
        return [[]]
    res = []
    if left > 0:
        last_res = helper(left-1, right)
        if last_res:
            for it in last_res:
                it.insert(0, '(')
            res.extend(last_res)
    if right > left:
        last_res = helper(left, right-1)
        if last_res:
            for it in last_res:
                it.insert(0, ')')
            res.extend(last_res)
    if res:
        return res
    return
res = f(3)
for it in res:
    print ''.join(it)
