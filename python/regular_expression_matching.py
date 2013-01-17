#! /usr/bin/env python
def f(s, p):
    if not s and not p:
        return True
    elif not s:
        if len(p) == 1 or p[1] != '*' or p[-1] != '*':
            return False
    if len(p) > 1:
        if p[1]!='*':
            if p[0] != '.':
                return s[0]==p[0] and f(s[1:], p[1:])
            else:
                return f(s[1:], p[1:])
        else:
            if p[0] != '.':
                cnt = 0
                res = False
                while cnt <= len(s):
                    res = True if f(s[cnt:], p[2:]) else res
                    cnt+=1
                return res
            else:
                return True
    else:
        if p[0] != '.':
            return s[0]==p[0] and f(s[1:], p[1:])
        else:
            return f(s[1:], p[1:])
print f("abcdede", "ab.*de")
