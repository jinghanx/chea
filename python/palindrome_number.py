#! /usr/bin/env python
def f(n):
    if n < 0:
        return False
    c = 1
    while n/c:
        c*=10
    c/=10
    flag = True
    while n:
        n1 = n/c
        n2 = n%10
        if n1!=n2:
            flag = False
            break
        else:
            n = n%c/10
            c/=100
    return flag
print f(-101)
