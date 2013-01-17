#! /usr/bin/env python
def f(s, target):
    if not s:
        return
    s.sort()
    res = helper(s, 0, target)
    for it in res:
        print it
def helper(s, index, target):
    if index == len(s):
        return
    cnt = 0
    res = []
    if index!=0 and s[index-1] == s[index]:
        return helper(s, index+1, target)
    while cnt*s[index] < target:
        last_res = helper(s, index+1, target - cnt*s[index])
        if last_res:
            for it in last_res:
                for i in range(cnt):
                    it.insert(0, s[index])
            res.extend(last_res)
        cnt += 1
    if cnt*s[index] == target:
        res.append([s[index]]*cnt)
    if not res:
        return
    return res
f([92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73], 310)
