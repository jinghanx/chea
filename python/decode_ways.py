#! /usr/bin/env python
def f(l):
    if not l:
        return 0
    s = [0 for i in range(len(l))]
    for i in range(len(l)-1, -1, -1):
        if l[i] != '0':
            if i != len(l) - 1:
                s[i] += s[i+1]
            else:
                s[i] += 1
        else:
            continue
        if i!= len(l) - 1:
            if l[i] == '1' or (l[i] == '2' and l[i+1] <= '6'):
                if i!= len(l)-2:
                    s[i] += s[i+2]
                else:
                    s[i] += 1
    return s[0]
print f('4673351343232714528787622144828949686814115978657763689251918941228645575658338815495647817194659205')
