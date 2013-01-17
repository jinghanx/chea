#! /usr/bin/env python
def f(l):
    if not l:
        return
    prev = None
    index_1 = None
    index_2 = l
    while index_2:
        if index_2.value != prev:
            if not index_1:
                index_1 = l
            else:
                index_1.next = index_2
                index_1 = index_1.next
            prev = index_2.value
        index_2 = index_2.next
    index_1.next = None
    return l
