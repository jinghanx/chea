#! /usr/bin/env python

def f(a,b,c):
    ai=0
    bi=0
    ci=0
    while ci<len(c):
        if a[ai] == c[ci]:
            ai+=1
        else if b[bi] == c[ci]:
            bi+=1
        else:
            return False
        ci+=1
    if ai!=len(a) or bi!=len(b):
        return False
    return True
