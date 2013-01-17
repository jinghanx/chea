#! /usr/bin/env python
def f(mat, h, w, k):
    if h<=0 or w <= 0:
        return
    if h==1:
        for i in range(w):
            print mat[k][k+i],
    elif w==1:
        for i in range(h):
            print mat[k+i][k],
    else:
        for i in range(w-1):
            print mat[k][k+i],
        for i in range(h-1):
            print mat[k+i][k+w-1],
        for i in range(w-1):
            print mat[k+h-1][k+w-i-1],
        for i in range(h-1):
            print mat[k+h-1-i][k],
    f(mat, h-2, w-2, k+1)

mat = [[1,2,3],[4,5,6],[7,8,9]]
f(mat,3,3,0)
