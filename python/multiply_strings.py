#! /usr/bin/env python
import sys
def f(s1, s2):
    flag = True
    if s1[0] == '-' and s2[0] == '-':
        s1=s1[1:]
        s2=s2[1:]
    elif s1[0]!='-' and s2[0] !='-':
        pass
    elif s1[0]=='-':
        s1=s1[1:]
        flag=False
    elif s2[0]=='-':
        s2=s2[1:]
        flag=False
    res= [0 for i in range(len(s1)+len(s2))]
    for i in range(len(s1)-1, -1, -1):
        carry = 0
        for j in range(len(s2)-1, -1, -1):
            ans = int(s1[i]) * int(s2[j])+carry+res[i+j+1]
            carry = ans/10
            res[i+j+1] = ans%10
        res[i]=carry
    if not flag:
        res.insert(0,'-')
    print res
def f2(s1, s2):
    if not s1 or not s2:
        return
    ans = [0 for i in range(len(s1)+len(s2))]
    for i in range(len(s1)-1, -1, -1):
        carry = 0
        for j in range(len(s2)-1, -1, -1):
            pro = int(s1[i])*int(s2[j])+carry+ans[i+j+1]
            carry = pro/10
            ans[i+j+1] = pro%10
        ans[i]=carry
    i = 0
    while i < len(ans):
        if ans[i] == 0:
            del ans[i]
        else:
            break
    print ans
f("123456789", "1")
f2("123456789", "1")
