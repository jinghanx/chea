#! /usr/bin/env python
def f(n, k, index):
    if not k:
        return [[]]
    if index == n + 1:
        return
    res = []
    last_res = f(n, k, index+1)
    if last_res:
        res.extend(last_res)
    last_res = f(n, k-1, index+1)
    if last_res:
        for it in last_res:
            it.insert(0, index)
        res.extend(last_res)
    return res if res else None
res = f(4, 2, 1)
for it in res:
    print it
