#! /usr/bin/env python
def f(s, t):
    if not s or not t:
        return
    if len(t) > len(s):
        return
    for i in range(len(s)-len(t)+1):
        flag = True
        for j in range(len(t)):
            if s[i+j] != t[j]:
                flag = False
                break
        if flag:
            return s[i:]
print f("mississippi", "issip")
