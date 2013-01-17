#! /usr/bin/env python
def f(l):
    if not l:
        return
    d = {}
    for it in l:
        sort_it = ''.join(sorted(it))
        if not d.get(sort_it):
            d[sort_it] = []
        d[sort_it].append(it)
    res = []
    for key in d:
        if len(d[key]) > 1:
            res.append(d[key])
    for it in res:
        print it
l = ['abc','acb','cba','sf','la','vvc','cvv','vcv','aaa','aaa','gghh','hghg']
f(l)
