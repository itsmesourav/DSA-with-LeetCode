class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n = len(grid)
        m = len(grid[0])

        flat = []
        for i in range(n):
            for j in range(m):
                flat.append(grid[i][j])

        f = len(flat)
        p = [1] * f
        s = [1] * f

        for i in range(1, f):
            p[i] = (p[i - 1] * flat[i - 1]) % MOD

        for i in range(f - 2, -1, -1):
            s[i] = (s[i + 1] * flat[i + 1]) % MOD

        res = [[1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res[i][j] = (p[i*m + j] * s[i*m + j]) % MOD
                
        return res
        