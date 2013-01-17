#! /usr/bin/env pyhon
def f(n):
    if not n:
        return
    res = [[1]]
    for i in range(1, n):
        tmp = []
        tmp.append(1)
        for j in range(len(res[i-1])-1):
            tmp.append(res[i-1][j]+res[i-1][j+1])
        tmp.append(1)
        res.append(tmp)
    return res
res = f(5)
for it in res:
    print it
