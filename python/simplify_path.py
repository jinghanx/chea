#! /usr/bin/env python
def f(s):
    combo = s.split('/')
    filter_combo = []
    for it in combo:
        if it =='..':
            if filter_combo:
                filter_combo.pop()
        elif it and it!='.':
                filter_combo.append(it)
    res = ''
    for it in filter_combo:
        res = res + '/'+it
    if not res:
        return '/'
    return res
print f('/home//foo/')
