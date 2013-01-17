#! /usr/bin/env python
import sys
def f(l):
    if not l:
        return 0
    s = [-1 for i in range(len(l))]
    for i in range(len(l)-1, -1, -1):
        if i == len(l)-1:
            s[i] = 0
        else:
            for j in range(1, l[i]+1):
                if i+j<len(l):
                    if s[i+j] == -1:
                        pass
                    elif s[i] == -1:
                        s[i] = 1+s[i+j]
                    else:
                        s[i] = min(s[i], s[i+j]+1)
    print s[0]
f([9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5])
