from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()

        def dfs(r, c):
            stack = [(r, c)]
            visited.add((r, c))

            while stack:
                row, col = stack.pop()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        board[nr][nc] == "X" or
                        (nr, nc) in visited
                    ):
                        continue

                    visited.add((nr, nc))
                    stack.append((nr, nc))

        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"