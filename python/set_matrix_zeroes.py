#! /usr/bin/env python
def f(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==0:
                mat[0][j]=0
                mat[i][0]=0
    for i in range(len(mat)):
        if mat[i][0]==0:
            for j in range(1, len(mat[0])):
