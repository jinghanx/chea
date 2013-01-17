#! /usr/bin/env python
def helper(mat, h, w, k, start):
    if h<=0 or w<=0:
        return
    if h==1:
        for i in range(w):
            start+=1
            mat[k][k+i]=start
    elif w==1:
        for i in range(h):
            start+=1
            mat[k+i][k]=start
    else:
        for i in range(w-1):
            start+=1
            mat[k][k+i] = start
        for i in range(h-1):
            start+=1
            mat[k+i][k+w-1] = start
        for i in range(w-1):
            start+=1
            mat[k+h-1][k+w-1-i]=start
        for i in range(h-1):
            start+=1
            mat[k+h-1-i][k]=start
    helper(mat, h-2, w-2, k+1, start)

def f(n):
    mat = [[0 for i in range(n)] for j in range(n)]
    helper(mat, n, n, 0, 0)
    for it in mat:
        print it
f(5)
