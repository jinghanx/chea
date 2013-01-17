#! /usr/bin/env python
def f(intervals, it):
    if not it:
        return intervals
    if not intervals:
        return [it]
    for i in range(len(intervals)):
        if intervals[i][1] < it[0]:
            continue
        if intervals[i][0] < it[0]:
            if it[1] < intervals[i][1]:
                return intervals
            else:
                start = intervals[i][0]
        else:
            start = it[0]
