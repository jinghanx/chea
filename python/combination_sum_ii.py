#! /usr/bin/env python
def f(s, index, target, prev_used):
    if not s:
        return
    if not target:
        return [[]]
    if index == len(s):
        return
    res = []
    if index == 0 or s[index] != s[index-1] or prev_used:
        last_res = f(s, index+1, target, False)
        if last_res:
            res.extend(last_res)
        last_res = f(s, index+1, target-s[index], True)
        if last_res:
            for it in last_res:
                it.insert(0, s[index])
            res.extend(last_res)
    else:
        last_res = f(s, index+1, target, False)
        if last_res:
            res.extend(last_res)
    if res:
        return res
    else:
        return
s = [10,1,2,7,6,1,5]
s.sort()
res = f(s, 0, 8, False)
for it in res:
    print it
