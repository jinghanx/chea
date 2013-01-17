#! /usr/bin/env python
def f(l):
    l_sort = sorted(l)
    mat = [[0 for j in range(len(l))] for i in range(len(l_sort))]
    for i in range(len(l)):
        for j in range(len(l_sort)):
            if i == 0 and j == 0:
                mat[i][j] = 1 if l[i] == l_sort[j] else 0
            elif i == 0:
                mat[i][j] = 1 if l[i] == l_sort[j] or mat[i][j-1] else 0
            elif j == 0:
                mat[i][j] = 1 if l[i] == l_sort[j] or mat[i-1][j] else 0
            else:
                if l[i] == l_sort[j]:
                    mat[i][j] = mat[i-1][j-1] + 1
                else:
                    mat[i][j] = max(mat[i-1][j], mat[i][j-1])
    def g(m,n):
        if m==0 and n==0:
            if l[m] == l_sort[n]:
                return [l[m]]
            else:
                return []
        elif m == 0:
            if l[m] == l_sort[n]:
                 return [l[m]]
            else:
                 return g(m, n-1)
        elif n == 0:
            if l[m] == l_sort[n]:
                 return [l[m]]
            else:
                 return g(m-1, n)
        else:
            if l[m] == l_sort[n]:
                return g(m-1, n-1) + [l[m]]
            else:
                if mat[m-1][n] > mat[m][n-1]:
                    return g(m-1, n)
                else:
                    return g(n-1, m)
    print g(len(l)-1,len(l_sort)-1)

f([0, 8, 2, 12, 4, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
