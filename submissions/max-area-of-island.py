# Problem #695: Max Area of Island
# Difficulty : Medium
# Language   : python3
# Runtime    : 15 ms
# Memory     : 19.4 MB
# URL        : https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = ((1,0), (-1,0), (0,1), (0,-1))

        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = 0
            area = 1

            while stack:
                row, col = stack.pop()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    if grid[nr][nc] == 0:
                        continue

                    grid[nr][nc] = 0
                    stack.append((nr, nc))
                    area += 1

            return area

        ans = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    ans = max(ans, dfs(r, c))

        return ans