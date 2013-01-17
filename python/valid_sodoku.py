#! /usr/bin/env python

#only need to check rows, cols and 3*3 cells, no need to check the unfilled cells,
#it seems like any given soduku, only if the given cells are valid, there is always
#solution for it
#which is really weird!!!

def f(board):
    #check rows
    for i in range(9):
        flag = [0 for cell in range(9)]
        for  j in range(9):
            if board[i][j] == '.':
                continue
            if flag[board[i][j]-1]:
                return False
            else:
                flag[board[i][j]-1] = 1
    #check columns
    for i in range(9):
        flag = [0 for cell in range(9)]
        for  j in range(9):
            if board[j][i] == '.':
                continue
            if flag[board[j][i]-1]:
                return False
            else:
                flag[board[j][i]-1] = 1
    #check 3*3 cells
    for i in range(9):
        flag = [0 for cell in range(9)]
        for j in range(3):
            for k in range(3):
                if board[i/3*3 + j][i%3*3 + k] == '.':
                    continue
                if flag[board[i/3*3 + j][i%3*3 + k]-1]:
                    return False
                else:
                   flag[board[i/3*3 + j][i%3*3 + k]-1] = 1
    return True
board = [
            [5,3,'.','.',7,'.','.','.','.'],
            [6,'.','.',1,9,5,'.','.','.'],
            ['.',9,8,'.','.','.','.',6,'.'],
            [8,'.','.','.',6,'.','.','.',3],
            [4,'.','.',8,'.',3,'.','.',1],
            [7,'.','.','.',2,'.','.','.',6],
            ['.',6,'.','.','.','.',9,8,'.'],
            ['.','.','.',4,1,9,'.','.',5],
            ['.','.','.','.',8,'.','.',7,9]
        ]
print f(board)
