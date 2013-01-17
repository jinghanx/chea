#! /usr/bin/env python
def g(left, right):
    if not left and not right:
        return True
    elif not left or not right:
        return False
    return left.value == right.value &&
            g(left.left, right.right) &&
            g(left.right, right.left)
