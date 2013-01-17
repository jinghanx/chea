#! /usr/bin/env python
def f(l1, l2):
    if not l1 and not l2:
        return
    elif not l1:
        return l2
    elif not l2:
        return l1
    res = None
    it1= l1
    it2= l2
    it3 = None
    while it1 and it2:
        if not it3:
            if it1.value < it2.value:
                it3 = it1
                res = it1
                it1 = it1.next
            else:
                it3 = it2
                res = it2
                it2 = it2.next
        else:
            if it1.value < it2.value:
                it3.next = it1
                it3 = it3.next
                it1 = it1.next
            elif:
                it3.next = it2
                it3 = it3.next
                it2 = it2.next
    while it1:
        it3.next = it1
        it3 = it3.next
        it1 = it1.next
    while it2:
        it3.next = it2
        it3 = it3.next
        it2 = it2.next
    return res
