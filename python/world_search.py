#! /usr/bin/env python
#brute force
def f(board, string, i, j, index, pass_route):
    if index == len(string):
        return True
    res = False
    if board[i][j] == string[index]:
        pass_route[(i,j)] = True
        if i > 0:
            if (i-1,j) not in pass_route:
                res = res if not f(board, string, i-1, j, index+1, pass_route) else True
        if i < len(board)-1:
            if (i+1, j) not in pass_route:
                res = res if not f(board, string, i+1, j, index+1, pass_route) else True
        if j > 0:
            if (i, j-1) not in pass_route:
                res = res if not f(board, string, i, j-1, index+1, pass_route) else True
        if j < len(board[0])-1:
            if (i, j+1) not in pass_route:
                res = res if not f(board, string, i, j+1, index+1, pass_route) else True
        del pass_route[(i, j)]
    return res

def help(board, string):
    res = False
    pass_route = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            res = res if not f(board, string, i, j, 0, pass_route) else True
    return res

board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
string = 'ABCB'
print help(board, string)
