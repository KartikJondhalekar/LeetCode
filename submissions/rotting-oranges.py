# Problem #994: Rotting Oranges
# Difficulty : Medium
# Language   : python3
# Runtime    : 6 ms
# Memory     : 17.7 MB
# URL        : https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                
                if grid[i][j] == 2:
                    q.append([i, j])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != 1):
                        continue

                    grid[r][c] = 2
                    fresh -= 1
                    q.append([r, c])
            time += 1
            
        return time if fresh == 0 else -1