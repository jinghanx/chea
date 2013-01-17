#! /usr/bin/env python
import copy
def f(l, index):
    if index == len(l):
        return [[]]
    res = []
    last_res = f(l, index+1)
    if last_res:
        res.extend(last_res)
        copy_last_res = copy.deepcopy(last_res)
        for it in copy_last_res:
            it.append(l[index])
        res.extend(copy_last_res)
    return res
def f2(l):
    if not l:
        return
    res = [[]]
    for i in range(len(l)):
        tmp_res = copy.deepcopy(res)
        for it in tmp_res:
            it.append(l[i])
        res.extend(tmp_res)
    for it in res:
        print it

f2([1,2,3])
