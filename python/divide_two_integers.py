#! /usr/bin/env python
def f(a, b):
    if not a and not b:
        return 0
    elif not a:
        return len(b)
    elif not b:
        return len(a)
    mat = [[0 for i in range(len(a))] for j in range(len(b))]
    for i in range(len(b)-1, -1, -1):
        for j in range(len(a)-1, -1, -1):
            if i == len(b)-1 and j == len(a)-1:
                mat[i][j] = 0 if b[i]==a[j] else 1
            elif i == len(b)-1:
                mat[i][j] = mat[i][j] + 1
            elif j == len(a)-1:
                mat[i][j] = mat[i+1][j] + 1
            else:
                mat[i][j] = min(mat[i+1][j]+1, mat[i][j+1]+1, mat[i+1][j+1] if b[i]==a[j] else mat[i+1][j+1]+1)
    for it in mat:
        print it
f("prosperity", "properties")
