
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    stack = [(r, c)]
                    total = 0

                    # Mark the starting cell as visited
                    total += grid[r][c]
                    grid[r][c] = 0

                    while stack:
                        x, y = stack.pop()

                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy

                            if (0 <= nx < m and 0 <= ny < n
                                    and grid[nx][ny] > 0):
                                total += grid[nx][ny]
                                stack.append((nx, ny))
                                grid[nx][ny] = 0

                    if total % k == 0:
                        islands += 1

        return islands
