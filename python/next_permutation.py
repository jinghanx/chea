#! /usr/bin/env python
def f(s):
    if not s:
        return
    i = len(s)-2
    while i!= -1:
        if s[i] < s[i+1]:
            break
        i -= 1
    if i == -1:
        s.reverse()
    else:
        j=len(s)-1
        while j > i:
            if s[j]>s[i] and (j==len(s)-1 or s[j+1] <= s[i]):
                break
            j-=1
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        s[i+1:] = list(reversed(s[i+1:]))
    return s
print f([2,2,7,5,4,3,2,2,1])
