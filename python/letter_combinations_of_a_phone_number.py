#! /usr/bin/env python
d = {
        1:[],
        2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z'],
        0:[' ']
        }
def f(s, index):
    if not s:
        return
    if index == len(s):
        return [[]]
    res = []
    for it in d.get(int(s[index])):
        last_res = f(s, index+1)
        if last_res:
            for elm in last_res:
                elm.insert(0, it)
            res.extend(last_res)
    return res
res = f('',0)
for it in res:
    print ''.join(it)
