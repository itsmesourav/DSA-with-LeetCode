
class Solution(object):
    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]
        answer = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or seen[i][j]:
                    continue

                stack = [(i, j)]
                seen[i][j] = True
                remainder = 0

                while stack:
                    x, y = stack.pop()
                    remainder = (remainder + grid[x][y]) % k

                    for nx, ny in ((x - 1, y), (x + 1, y),
                                   (x, y - 1), (x, y + 1)):
                        if (0 <= nx < m and 0 <= ny < n
                                and grid[nx][ny] > 0
                                and not seen[nx][ny]):
                            seen[nx][ny] = True
                            stack.append((nx, ny))

                if remainder == 0:
                    answer += 1

        return answer
