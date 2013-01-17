#! /usr/bin/env python
def f(s1, s2):
    if not s1 or not s2:
        return ''
    mat = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 or j == 0:
                continue
            else:
                if s1[i-1] == s2[j-1]:
                    mat[i][j] = mat[i-1][j-1] + 1
    mx = 0
    res = ''
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if mat[i][j] > mx:
                mx = mat[i][j]
                res = ''.join(s1[i-mx:i])
    print res
f('abab', 'baba')
