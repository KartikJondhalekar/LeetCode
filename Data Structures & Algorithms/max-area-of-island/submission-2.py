class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        maxArea = 0

        def bfs(r, c, currArea):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if (nr not in range(ROWS) or nc not in range(COLS) or grid[nr][nc] == 0):
                        continue

                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    currArea += 1

            return currArea

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    currArea = bfs(row, col, 1)
                    maxArea = max(maxArea, currArea)

        return maxArea

