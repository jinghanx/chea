#! /usr/bin/env python
def f(l):
    if not l:
        return False
    s = [False for i in range(len(l))]
    for i in range(len(l)-1, -1, -1):
        if i == len(l)-1:
            s[i] = True
        else:
            for j in range(1,l[i]+1):
                if i+j < len(l):
                    if s[i+j] == True:
                        s[i] = True
                        break
    print s[0]
f([3,2,1,0,4])
