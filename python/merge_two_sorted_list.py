#! /usr/bin/env python
def f(h1,h2):
    if h1.value < h2.value:
        res_h = h1
        h1 = h1.next
    else:
        res_h = h2
        h2 = h2.next
    it = res_h
    while not h1 and not h2:
        it h1.value < h2.value:
            it.next = h1
        else:
            it.next = h2
        it = it.next
    while not h1:
        it.next = h1
        it = it.next
    while not h2:
        it.next = h2
        it = it.next
    return res_h

