#! /usr/bin/env python
def f(s1, s2, l1, r1, l2, r2):
    if l1 > r1 and l2 > r2:
        return
    elif l1 > r1:
        if (r2-l2)%2:
            return float(s2[l2/2+r2/2])/2.0 + float(s2[l2/2+r2/2+1])/2.0
        return s2[l2/2+r2/2]
    elif l2 > r2:
        if (r1-l1)%2:
            return float(s1[l1/2+r1/2])/2.0 + float(s1[l1/2+r1/2+1])/2.0
        return s1[l1/2+r2/2]
    else:
        m1 = (l1+r1)/2
        m2 = (l2+r2)/2
        if s1[m1] == s2[m2]:
            return s1[m1]
        elif s1[m1] < s2[m2]:
            l1 = m1+1
            r2 = m2-1
            if l1 > r1 and l2 > r2:
                return float(s1[m1]+s2[m2])/2.0
            else:
                return f(s1,s2,l1,r1,l2,r2)
        else:
            r1 = m1-1
            l2 = m2+1
            if l1 > r1 and l2 > r2:
                return float(s1[m1]+s2[m2])/2.0
            else:
                return f(s1,s2,l1,r1,l2,r2)
print f([1], [2,3,4,5], 0, 0, 0, 3)

