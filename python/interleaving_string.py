#! /usr/bin/env python
def f(s1, s2, s3):
    if not s1:
        return True if s2 == s3 else False
    if not s2:
        return True if s1 == s3 else False
    if len(s3)!=len(s1)+len(s2):
        return False
    mat = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            if i == len(s1) and j == len(s2):
                mat[i][j] = True
            elif i==len(s1):
                mat[i][j] = s2[j]==s3[i+j] and mat[i][j+1]
            elif j==len(s2):
                mat[i][j] = s1[i]==s3[i+j] and mat[i+1][j]
            else:
                mat[i][j] = (s1[i]==s3[i+j] and mat[i+1][j]) or (s2[j]==s3[i+j] and mat[i][j+1])
    for it in mat:
        print it
s1 = "def"
s2 = ""
s3 = "defg"
f("ccabcaacaacccaabacbcacac", "ccbcbacbaaccabbabbca", "cccbccbabcacaacabacaaccccaaabbabbabccabcacac")
