#! /usr/bin/env python
roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

def f(n):
    offset = 0
    ans = ''
    while n:
        cur = n%10
        n /=10
        res= ''
        if cur == 9:
            res+=roman[offset]
            res+=roman[offset+2]
        elif cur == 4:
            res+=roman[offset]
            res+=roman[offset+1]
        else:
            if cur >= 5:
                res+=roman[offset+1]
                cur-=5
            for i in range(cur):
                res+=roman[offset]
        ans = res+ans
        offset+=2
    return ans
print f(27)
