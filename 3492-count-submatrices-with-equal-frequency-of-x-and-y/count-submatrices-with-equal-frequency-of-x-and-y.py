class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        res = 0
        x = [[0] * m for _ in range(n)]
        y = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                x[i][j] = (
                    (x[i - 1][j] if i > 0 else 0) +
                    (x[i][j - 1] if j > 0 else 0) -
                    (x[i - 1][j - 1] if i > 0 and j > 0 else 0) +
                    (1 if grid[i][j] == 'X' else 0)
                )

                y[i][j] = (
                    (y[i - 1][j] if i > 0 else 0) +
                    (y[i][j - 1] if j > 0 else 0) -
                    (y[i - 1][j -1] if i > 0 and j > 0 else 0) +
                    (1 if grid[i][j] == 'Y' else 0)
                )

                if x[i][j] and x[i][j] == y[i][j]:
                    res += 1

        return res