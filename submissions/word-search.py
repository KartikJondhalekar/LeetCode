# Problem #79: Word Search
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 19.4 MB
# URL        : https://leetcode.com/problems/word-search/

from collections import Counter
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # Count characters on the board
        board_count = Counter(ch for row in board for ch in row)

        # If the board doesn't contain enough of any character, it's impossible
        for ch, cnt in Counter(word).items():
            if board_count[ch] < cnt:
                return False

        # Start from the rarer end of the word
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i]
            ):
                return False

            temp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            board[r][c] = temp
            return found

        # Only start from cells matching the first character
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False