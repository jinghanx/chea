#! /usr/bin/env python
from node import node

def f(s1, s2):
    if not s1:
        return s2
    if not s2:
        return s1

    it1 = s1
    it2 = s2

    res = None
    carry = 0

    while it1 and it2:
        curr = it1.value + it2.value + carry
        carry = curr / 10
        value = curr % 10
        if not res:
            res = node(value)
            prev = res
        else:
            prev.next = node(value)
            prev = prev.next
        it1 = it1.next
        it2 = it2.next

    while it1:
        curr = it1.value + carry
        carry = curr / 10
        value = curr % 10
        prev.next = node(value)
        prev = prev.next
        it1 = it1.next

    while it2:
        curr = it2.value + carry
        carry = curr / 10
        value = curr % 10
        prev.next = node(value)
        prev = prev.next
        it2 = it2.next

    if carry:
        prev.next = node(carry)

    it = res
    while it:
        print it.value
        it = it.next
    return res
s1 = node(2)
s1.next = node(4)
s1.next.next = node(8)
s2 = node(5)
s2.next = node(6)
s2.next.next = node(4)

f(s1, s2)

