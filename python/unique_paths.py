#! /usr/bin/env python
def f(m, n):
    shorter = min(m,n)
    longer = max(m,n)
    s = [0 for i in range(shorter+1)]
    for i in range(longer-1, -1, -1):
        for j in range(shorter-1, -1, -1):
            if i == longer-1 and j == shorter-1:
                s[j] = 1
            else:
                s[j] = s[j] + s[j+1]
    return s[0]
print f(3,3)
