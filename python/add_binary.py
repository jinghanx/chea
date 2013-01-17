#! /usr/bin/env python
def f(s1, s2):
    if not s1:
        return s2
    if not s2:
        return s1
    carry = 0
    res = []
    it1 = len(s1) - 1
    it2 = len(s2) - 1
    while it1 != -1 and it2 != -1:
        c1 = int(s1[it1])
        c2 = int(s2[it2])
        if not carry:
            carry = c1 & c2
            value = c1 ^ c2
        else:
            carry = c1 | c2
            value = 1 - (c1 ^ c2)
        it1 -= 1
        it2 -= 1
        res.insert(0, str(value))

    while it1 != -1:
        c1 = int(s1[it1])
        if not carry:
            value = c1
        else:
            carry = c1
            value = 1 - c1
        it1 -= 1
        res.insert(0, str(value))

    while it2 != -1:
        c2 = int(s2[it2])
        if not carry:
            value = c2
        else:
            carry = c2
            value = 1 - c2
        it2 -= 1
        res.insert(0, str(value))
    if carry:
        res.insert(0, str(carry))
    print ''.join(res)
f('1','11')
