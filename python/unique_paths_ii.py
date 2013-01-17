#! /usr/bin/env python
def f(m, n, mat):
    shorter = min(m,n)
    longer = max(m,n)
    s = [0 for i in range(shorter+1)]
    for i in range(longer-1, -1, -1):
        for j in range(shorter-1, -1, -1):
            curr_block = mat[i][j] if m>n else mat[j][i]
            if not mat[i][j]:
                if i == longer-1 and j == shorter-1:
                    s[j] = 1
                else:
                    s[j] = s[j] + s[j+1]
            else:
                s[j] = 0
        print s
    return s[0]
m = 3
n = 3
mat = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
        ]
print f(3,3,mat)
