#! /usr/bin/env python
# dynamic programming classic
#def f(l):
#    mat =[[-1 for j in range(len(l))] for i in range(len(l))]
#    for i in range(len(l)):
#        for j in range(len(l)):
#            if i == j:
#                if l[i] == '(':
#                    mat[i][j] = 1
#    mx = 0
#    for N in range(1, len(l)):
#        for i in range(len(l) - N):
#            j = i + N
#            if mat[i][j-1] != -1:
#                if l[j] == '(':
#                    mat[i][j] = mat[i][j-1] + 1
#                else:
#                    mat[i][j] = mat[i][j-1] - 1
#                if not mat[i][j]:
#                    mx = max(mx, j-i+1)
#    return mx
def f(l):
    mat = [[0 for i in range(len(l))] for j in range(len(l))]
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] == '(':
                mat[i][j] = 1
    mx = 0
    for N in range(1, len(l)-1):
        for i in range(len(l)-N):
            j = i+N
            if not mat[i][j-1]:
                pass
            else:
                if l[j] == '(':
                    mat[i][j] = mat[i][j-1]+1
                else:
                    mat[i][j] = mat[i][j-1]-1
                    if mat[i][j] == 0:
                        mx = max(mx, N+1)
    return mx
print f(")(((((()())()()))()(()))(")
