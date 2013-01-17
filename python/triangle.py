#! /usr/bin/env python
def f(triangle, level, index):
    if level == len(triangle):
        return 0
    tmp_mini_1 = f(triangle, level+1, index) + triangle[level][index]
    tmp_mini_2 = f(triangle, level+1, index+1) + triangle[level][index]
    return min(tmp_mini_1, tmp_mini_2)
def f2(t):
    mat = [[0 for j in range(len(t[i]))] for i in range(len(t))]
    for i in range(len(t)-1, -1, -1):
        for j in range(len(t[i])):
            if i == len(t)-1:
                mat[i][j] = t[i][j]
            else:
                mat[i][j] = min(mat[i+1][j], mat[i+1][j+1]) + t[i][j]
    for it in mat:
        print it
triangle = [
               [2],
               [3,4],
               [6,5,7],
               [4,1,8,3]
           ]
f2(triangle)
print f(triangle, 0, 0)
