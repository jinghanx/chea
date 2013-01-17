#! /usr/bin/env python
# use left index and right index to keep track the length
#def f(l):
#    left = 0
#    right = 0
#    flag_mat = [False for i in range(26)]
#    mx = 0
#    while right != len(l):
#        while not flag_mat[ord(l[right])-97]:
#            flag_mat[ord(l[right])-97] = True
#            right += 1
#            if right == len(l):
#                break
#        tmp_mx = right - left
#        mx = max(tmp_mx, mx)
#        while l[left] != l[right]:
#            flag_mat[ord(l[left])-97] = False
#            left += 1
#        left += 1
#        right += 1
#    mx = max(right - left, mx)
#    return mx
def f(l):
    if not l:
        return
    left = 0
    right = 0
    longest = 0
    lleft = 0
    lright = 0
    d = dict()
    while right != len(l):
        while not d.get(l[right]):
            d[l[right]] = True
            right += 1
        right+=1
        if longest < right - left -1:
            longest = right - left -1
            lleft = left
            lright = right-2
        while l[left] != l[right]:
            del d[l[left]]
            left += 1
        left += 1
    if longest < right - left:
        longest = right - left
        lleft = left
        lright = right-2
    print lleft, lright

print f('bbbb')
