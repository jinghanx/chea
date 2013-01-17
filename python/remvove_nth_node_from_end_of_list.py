#! /usr/bin/env python
def f(n,target):
    if not n:
        return
    it1 = n
    it2 = n
    cnt = 1
    while it1 and cnt<target:
