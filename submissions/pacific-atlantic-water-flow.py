# Problem #417: Pacific Atlantic Water Flow
# Difficulty : Medium
# Language   : python3
# Runtime    : 39 ms
# Memory     : 22.8 MB
# URL        : https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                heights[r][c] < prevHeight):
                return

            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) in pac and (r, c) in atl):
                    res.append([r, c])

        return res