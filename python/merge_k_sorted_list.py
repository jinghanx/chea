#! /usr/bin/env python
import heapq
def f(lists):
    if not lists:
        return
    length = len(lists)
    heap = []
    for it in lists:
        heaqp.heappush(heap,it, key=operator.attrgetter(
