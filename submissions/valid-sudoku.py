# Problem #36: Valid Sudoku
# Difficulty : Medium
# Language   : python3
# Runtime    : 5 ms
# Memory     : 17.7 MB
# URL        : https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))