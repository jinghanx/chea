#! /usr/bin/env python
def f(pat, string, i1, i2):
    if i1 == len(pat) and i2 == len(string):
        return True
    elif i1 == len(pat):
        return False
    if pat[i1] == '*':
        res = False
        while i2 <= len(string):
            res =  True if f(pat, string, i1+1, i2) else res
            i2 += 1
        return res
    elif i2 == len(string):
        return False
    elif pat[i1] != '?':
        return pat[i1]==string[i2] and f(pat,string,i1+1,i2+1)
    elif pat[i1] == '?':
        return f(pat, string, i1+1, i2+1)

print f("c*a*b", "aab", 0, 0)
