#! /usr/bin/env python
import sys
def f(l):
    s = []
    left_edge = []
    right_edge = []
    for i in range(len(l)):
        while s:
            if l[s[-1]] >= l[i]:
                s.pop()
            else:
                break
        if s:
            left_edge.append(s[-1]+1)
        else:
            left_edge.append(i)
        s.append(i)
    s = []
    for i in range(len(l)-1, -1, -1):
        while s:
            if l[s[-1]] >= l[i]:
                s.pop()
            else:
                break
        if s:
            right_edge.append(s[-1]-1)
        else:
            right_edge.append(i)
        s.append(i)
    right_edge.reverse()
    mx = -sys.maxint
    for i in range(len(l)):
        tmp = l[i] * (right_edge[i] - left_edge[i] + 1)
        mx = max(mx, tmp)
    return mx
print f([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])
