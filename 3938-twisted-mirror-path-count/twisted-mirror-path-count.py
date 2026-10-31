
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # Destination after entering a cell while moving right/down
        right = [[-1] * n for _ in range(m)]
        down = [[-1] * n for _ in range(m)]

        # Precompute mirror movements
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if grid[i][j] == 0:
                    right[i][j] = i * n + j
                    down[i][j] = i * n + j

                else:
                    # Entered mirror while moving right:
                    # move to the cell below
                    if i + 1 < m:
                        right[i][j] = down[i + 1][j]

                    # Entered mirror while moving down:
                    # move to the cell on the right
                    if j + 1 < n:
                        down[i][j] = right[i][j + 1]

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                ways = dp[i][j]

                if ways == 0:
                    continue

                # Move right
                if j + 1 < n:
                    pos = right[i][j + 1]

                    if pos != -1:
                        x, y = divmod(pos, n)
                        dp[x][y] = (dp[x][y] + ways) % MOD

                # Move down
                if i + 1 < m:
                    pos = down[i + 1][j]

                    if pos != -1:
                        x, y = divmod(pos, n)
                        dp[x][y] = (dp[x][y] + ways) % MOD

        return dp[m - 1][n - 1]
