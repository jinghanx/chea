#! /usr/bin/env python
def f(s, n):
    mat = [[] for i in range(n)]
    cnt_unit = 2*n-2
    for i in range(len(s)):
        j = i%cnt_unit
        k = j if j<n else n-(j-n+2)
        mat[k].append(s[i])
    res = []
    for it in mat:
        print it
print f("PAYPALISHIRING", 3)
