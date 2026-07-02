class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.pop()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if (nr not in range(rows) or nc not in range(cols) or grid[nr][nc] == "0"):
                        continue

                    q.append((nr, nc))
                    grid[nr][nc] = "0"
            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    islands += 1

        return islands