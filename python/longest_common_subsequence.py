#! /usr/bin/env python
def f(s, t):
    if not s or not t:
        return
    mat = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if i == 0 or j == 0:
                pass
            elif s[i-1] == t[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i][j-1], mat[i-1][j])
    def g(m,n):
        if m==0 or n==0:
            return []
        elif s[m-1]==t[n-1]:
            return g(m-1,n-1)+ [s[m-1]]
        elif mat[m-1][n] > mat[m][n-1]:
            return g(m-1,n)
        else:
            return g(m,n-1)
    print g(len(s),len(t))
#f('avbf','af')
