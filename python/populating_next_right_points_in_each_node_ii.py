#! /usr/bin/env python
def f(r):
    if not r:
        return
    if r.left:
        if r.right:
            r.left.next = r.right
        tmp_next = r.next
        while tmp_next:
            if tmp_next.left:
                r.left=tmp_next.left
                break
            elif tmp_next.right:
                r.left=tmp_next.right
                break
            tmp_next=tmp_next.next
    if r.right:
        tmp_next=r.next
        while tmp_next:
            if tmp_next.left:
                r.right=tmp_next.left
                break
            elif tmp_next.right:
                r.right=tmp_next.right
                break
            tmp_next=tmp_next.next
    f(r.left)
    f(r.right)


