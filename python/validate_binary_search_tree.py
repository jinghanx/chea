#! /usr/bin/env python
def f(r, mi, mx):
    if not r:
        return False
    return r.value > mi and r.value < mx and f(r.left, mi, r.value) and f(r.right, r.value, mx)
