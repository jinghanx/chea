#! /usr/bin/env python
def f(s):
    if not s:
        return 0
    length = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == ' ':
            continue
        else:
            break
    for j in range(i, -1, -1):
        if s[j] != ' ':
            length += 1
        else:
            break
    return length
print f("        ")
