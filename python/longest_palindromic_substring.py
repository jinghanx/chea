#! /usr/bin/env python
# dynamic programming classic
#def f(l):
#    mat = [[0 for j in range(len(l))] for i in range(len(l))]
#    for i in range(len(l)):
#        for j in range(len(l)):
#            if i == j:
#                mat[i][j] = 1
#            if i == j-1:
#                if l[i] == l[j]:
#                    mat[i][j] = 2
#    mx = 0
#    for N in range(2, len(l)):
#        for i in range(len(l)-N):
#            j = i + N
#            if l[i] == l[j] and mat[i+1][j-1]:
#                mat[i][j] = mat[i+1][j-1] + 2
#                mx = max(mx, mat[i][j])
#    return mx
def f(l):
    if not l:
        return
    mat = [[0 for i in range(len(l))]for j in range(len(l))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j:
                mat[i][j] = 1
            if i == j-1:
                mat[i][j] = 2 if l[i] == l[j] else 0
    for length in range(2, len(l)):
        for i in range(len(l)-length):
            j = i + length
            if l[i] == l[j]:
                if mat[i+1][j-1]:
                    mat[i][j] = mat[i+1][j-1]+2
    mx_length = 0
    left = 0
    right = 0
    for i in range(len(l)):
        for j in range(len(l)):
            if j>=i:
                if mat[i][j] > mx_length:
                    mx_length = mat[i][j]
                    left = i
                    right = j
    return l[left:right+1]

print f("bananas")
