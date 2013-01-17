#! /usr/bin/env python
from node import node
def f(l):
    if not l:
        return
    if not l.next:
        return l
    n = l.next
    n2 = n.next
    n.next = l
    l.next = f(n2)
    return n

a = node(1)
b = a
a.next = node(2)
a = a.next
a.next = node(3)
a = a.next
a.next = node(4)
it = f(b)
print it.value
print it.next.value
print it.next.next.value
print it.next.next.next.value
