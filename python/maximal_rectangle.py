#! /usr/bin/env python
import sys
def f(mat):
    mx = -sys.maxint
    s = [0 for i in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]=='1':
                s[j]+=1
            else:
                s[j] = 0
        print s
        mx = max(mx, helper(s))
    return mx
def helper(s):
    stack = []
    left = []
    right = []
    for i in range(len(s)):
        while stack:
            if s[stack[-1]] >= s[i]:
                stack.pop()
            else:
                break
        if stack:
            left.append(stack[-1]+1)
        else:
            left.append(i)
        stack.append(i)
    stack=[]
    for i in range(len(s)-1,-1,-1):
        while stack:
            if s[stack[-1]] >= s[i]:
                stack.pop()
            else:
                break
        if stack:
            right.append(stack[-1]-1)
        else:
            right.append(i)
        stack.append(i)
    right.reverse()
    mx = -sys.maxint
    for i in range(len(s)):
        mx = max(mx, s[i]*(right[i]-left[i]+1))
    return mx
mat = ["0010","1111","1111","1110","1100","1111","1110"]
s = [6,6,2,0]
print helper(s)
