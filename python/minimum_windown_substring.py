#! /usr/bin/env python
def f(s, t):
    if not t or not s:
        return ""
    hist = {}
    hist_2 = {}
    for it in t:
        if not hist.get(t):
            hist[t] = 0
        hist[t] += 1
    start = 0
    end = 0
    while end != len(s):
