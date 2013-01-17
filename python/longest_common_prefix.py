#! /usr/bin/env python
def f(array):
    if not array:
        return 0
    for i in range(len(array[0])):
        flag = True
        curr_val = array[0][i]
        for it in array:
            if i >= len(it) or it[i]!=curr_val:
                flag = False
                break
        if not flag:
            i = i-1
            break
    return array[0][:i+1]
print f(["aaa","aa","aaa"])

