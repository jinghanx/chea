#! /usr/bin/env python
def f(l):
    s = [False]*len(l)
    s[-1] = True
    for i in range(len(l)-2, -1, -1):
        flag =False
        for j in range(1, l[i]+1):
            if i+j<len(l) and s[i+j]:
                flag =True
        if flag:
            s[i]=True
    if s[0] == True:
        return True
    return False
print f([3,2,1,0,4])
