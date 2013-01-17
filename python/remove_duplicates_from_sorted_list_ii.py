#! /usr/bin/env python
def f(l):
    if not l:
        return
    prev = l
    cnt = 0
    index_1 = None
    index_2 = l
    res = None
    while index_2:
        if prev.value!=index_2.value:
            if cnt==1:
                if not index_1:
                    res = prev
                    index_1=prev
                else:
                    index_1.next=prev
                    index_1=index_1.next
            prev = index_2
            cnt = 1
        else:
            if index_1:
                cnt += 1
            else:
                cnt = 1
        index_2 = index_2.next
    index_1.next = None
    return res
