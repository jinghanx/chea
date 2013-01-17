#! /usr/bin/env python
def f(n):
    if n == 0:
        return ''
    if n == 1:
        return '1'
    res = ['1']
    for i in range(n-1):
        tmp_res = []
        prev = None
        cnt = 0
        for j in range(len(res)):
            if res[j] == prev:
                cnt += 1
                prev = res[j]
            else:
                if cnt:
                    tmp_res.append(str(cnt))
                    tmp_res.append(prev)
                prev = res[j]
                cnt = 1
        tmp_res.append(str(cnt))
        tmp_res.append(prev)
        res = tmp_res
    return ''.join(res)
print f(3)
