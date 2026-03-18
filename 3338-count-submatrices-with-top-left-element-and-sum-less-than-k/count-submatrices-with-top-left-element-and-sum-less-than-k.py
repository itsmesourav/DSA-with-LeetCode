class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        ps = [[0] * m for _ in range(n)]
        ps[0][0] = grid[0][0]

        res = 1 if ps[0][0] <= k else 0

        for j in range(1, m):
            ps[0][j] = grid[0][j] + ps[0][j - 1]
            if ps[0][j] <= k:
                res += 1

        for i in range(1, n):
            ps[i][0] = grid[i][0] + ps[i - 1][0]
            if ps[i][0] <= k:
                res += 1

        for i in range(1, n):
            for j in range(1, m):
                ps[i][j] = grid[i][j] +(
                    ps[i - 1][j] +
                    ps[i][j - 1] -
                    ps[i - 1][j - 1]
                ) 

                if ps[i][j] <= k:
                    res += 1
        
        return res