#! /usr/bin/env python
def f(n):
    cnt_2 = 0
    res = 0
    while cnt_2*2 <= n:
        res += helper(n-cnt_2*2, cnt_2)
        cnt_2 += 1
    return res
def helper(cnt_1, cnt_2):
    return factorial(cnt_1+cnt_2)/factorial(cnt_1)/factorial(cnt_2)
def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)
print f(10)
