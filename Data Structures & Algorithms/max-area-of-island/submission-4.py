class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        maxArea = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            currArea = 1

            while q:
                row, col = q.pop()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if (nr not in range(ROWS) or nc not in range(COLS) or grid[nr][nc] == 0):
                        continue

                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    currArea += 1

            return currArea

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    currArea = bfs(row, col)
                    maxArea = max(currArea, maxArea)

        return maxArea

