#! /usr/bin/env python
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def f(left, right):
    if left > right:
        return [None]
    res = []
    for it in range(left, right+1):
        left_res = f(left, it-1)
        right_res = f(it+1, right)
        for left_node in left_res:
            for right_node in right_res:
                rt = node(it)
                rt.left = left_node
                rt.right = right_node
                res.append(rt)
    return res

def level_print(rt):
    res = []
    queue = []
    queue.append(rt)
    res.append(queue)
    while 1:
        next_queue = []
        for node in queue:
            if node == '#':
                continue
            if node.left:
                next_queue.append(node.left)
            else:
                next_queue.append('#')
            if node.right:
                next_queue.append(node.right)
            else:
                next_queue.append('#')
        if not next_queue:
            break
        res.append(next_queue)
        queue = next_queue
    for level in res:
        for node in level:
            if node == '#':
                print '#',
            else:
                print node.value,
        print

def print_res(res):
     for res in res_list:
         level_print(res)
         print

res_list = f(1,3)
print_res(res_list)
