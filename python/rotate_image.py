#! /usr/bin/env python
def f(mat):
    if not mat:
        return
    h = len(mat)
    for i in range(h/2):
        for j in range(i, h-i-2):

