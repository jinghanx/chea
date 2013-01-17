#! /usr/bin/env python
def f(s, t):
    mat = [[0 for i in range(len(t))] for j in range(len(s))]
    for i in range(len(s)-1, -1, -1):
        for j in range(len(t)-1, -1, -1):
            if i == len(s)-1 and j == len(t)-1:
                mat[i][j] = 1
            elif i == len(s) - 1:
                if s[i] == t[j]:
                    mat[i][j] = 1
                else:
                    mat[i][j] = 0
            elif j == len(t) - 1:
                if s[i] == t[j]:
                    mat[i][j] = 1 + mat[i+1][j]
                else:
                    mat[i][j] = mat[i+1][j]
            else:
                if s[i] == t[j]:
                    mat[i][j] = mat[i+1][j] + mat[i+1][j+1]
                else:
                    mat[i][j] = mat[i+1][j]
    for it in mat:
        print it
f("rabbbit", "rabbit")

