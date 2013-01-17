#! /usr/bin/env python
import sys
def f(l):
    if not l:
        print 'the list is empty'
        return
    max_profit = 0
    lowest = sys.maxint
    for it in l:
        if (it - lowest) > max_profit:
            max_profit = it - lowest
        lowest = min(lowest, it)
    print max_profit
l = [3,5,3,2,5,6,3,5,6,7,1,4]
f(l)
