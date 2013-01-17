#! /usr/bin/env python
def f(mat):
    # corner case
    if not mat or not mat[0]:
        return

    height = len(mat)
    width = len(mat[0])
    shorter = min(height,width)
    longer = max(height,width)
    s = [0 for i in range(shorter)]

    for i in range(longer-1, -1, -1):
        for j in range(shorter-1, -1, -1):
            curr = mat[i][j] if shorter == width else mat[j][i]
            if i == longer-1:
                if j == shorter-1:
                    s[j] = curr
                else:
                    s[j] = s[j+1] + curr
            else:
                if j == shorter-1:
                    s[j] = s[j] + curr
                else:
                    s[j] = min(s[j], s[j+1]) + curr
    return s[0]

print f(mat)
