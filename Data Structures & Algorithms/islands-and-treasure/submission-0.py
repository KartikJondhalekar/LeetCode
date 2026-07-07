class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addStep(r, c):
            if ((r, c) in visited or
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == -1):
                return

            visited.add((r, c))
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
                    
        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    addStep(r + dr, c + dc)

            dist += 1