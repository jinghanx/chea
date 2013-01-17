#! /usr/bin/env python
def f(l):
    stack = []
    for it in l:
        if it == '(':
            stack.append(1)
        elif it == ')':
            if stack[-1] != 1:
                return False
            stack.pop()
        elif it == '[':
            stack.append(2)
        elif it == ']':
            if stack[-1] != 2:
                return False
            stack.pop()
        elif it == '{':
            stack.append(3)
        elif it == '}':
            if stack[-1] != 3:
                return False
            stack.pop()
    if stack:
        return False
    return True

print '()[]{}'
print f('()[]{}')
print '(]'
print f('(]')
print '([)]'
print f('([)]')
