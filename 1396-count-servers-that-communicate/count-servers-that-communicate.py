class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        r = [0] * m
        c = [0] * n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    r[i] += 1
                    c[j] += 1
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (r[i] > 1 or c[j] > 1):
                    ans += 1
        
        return ans