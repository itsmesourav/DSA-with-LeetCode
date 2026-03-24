class Solution(object):
    def constructProductMatrix(self, grid):
        MOD = 12345
        n = len(grid)
        m = len(grid[0])
        pre = [[1] * m for _ in range(n)]
        suf = [[1] * m for _ in range(n)]

        p = 1
        for i in range(n):
            for j in range(m):
                pre[i][j] = p
                p = (p * grid[i][j]) % MOD

        s = 1
        for i in range(n - 1, -1, -1):
            for j in range(m -1, -1, -1):
                suf[i][j] = s
                s = (s * grid[i][j]) % MOD

        for i in range(n):
            for j in range(m):
                pre[i][j] = (pre[i][j] * suf[i][j]) % MOD
    
        return pre