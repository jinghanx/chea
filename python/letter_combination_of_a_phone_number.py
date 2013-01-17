#! /usr/bin/env python
# notice str to int
# notice the copy of last_res if it is going to be used in current context a couple of times
# notice when to append, when to extend
import copy
d = {
        1: [],
        2: ['a','b','c'],
        3: ['d','e','f'],
        4: ['g','h','i'],
        5: ['j','k','l'],
        6: ['m','n','o'],
        7: ['p','q','r','s'],
        8: ['t','u','v'],
        9: ['w','x','y','z'],
        0: [' ']
    }
def f(l,index):
    if index == -1:
        return [[]]
    cur = l[index]
    comb = d.get(int(cur))
    res = []
    last_res = f(l, index-1)
    if last_res:
        for it in comb:
            copy_last_res = copy.deepcopy(last_res)
            for it2 in copy_last_res:
                it2.append(it)
            res.extend(copy_last_res)
    return res
print f('23', len('23')-1)
