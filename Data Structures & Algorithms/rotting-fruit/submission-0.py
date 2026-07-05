class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        time = fresh = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if (nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        grid[nr][nc] != 1):
                        continue

                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1