#! /usr/bin/env python
import copy
def f(s, index):
    if index == len(s):
        return [[]], 0
    last_res, length = f(s, index+1)
    add_last_res = []
    for i in range(len(last_res)):
        if index<len(s)-1:
            if s[index]!=s[index+1]:
                tmp = copy.deepcopy(last_res[i])
                tmp.insert(0,s[index])
                add_last_res.append(tmp)
            elif i>=length:
                tmp = copy.deepcopy(last_res[i])
                tmp.insert(0,s[index])
                add_last_res.append(tmp)
        else:
            tmp = copy.deepcopy(last_res[i])
            tmp.insert(0,s[index])
            add_last_res.append(tmp)

    length_last_res = len(last_res)
    last_res.extend(add_last_res)
    return last_res,length_last_res
def f2(s):
    if not s:
        return
    i = 0
    prev = None
    res = [[]]
    length = 0
    while i < len(s):
        if s[i] != prev:
            copy_res = copy.deepcopy(res)
            for it in copy_res:
                it.append(s[i])
            res.extend(copy_res)
            length = len(copy_res)
        else:
            copy_res = copy.deepcopy(res)
            copy_res = copy_res[-length:]
            for it in copy_res:
                it.append(s[i])
            res.extend(copy_res)
        prev = s[i]
        i+=1
    return res

res = f2([1,2,2])
for it in res:
    print it
