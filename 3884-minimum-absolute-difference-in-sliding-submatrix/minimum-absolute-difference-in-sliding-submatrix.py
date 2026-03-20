class Solution(object):
    def minAbsDiff(self, grid, k):
        n = len(grid)
        m = len(grid[0])
        res = [[0] * (m - k + 1) for _ in range(n - k + 1)] 
        
        for i in range(n):
            for j in range(m):
                if i + k <= n and j + k <= m:
                    curr = set()
                    for ii in range(i, i + k):
                        for jj in range(j, j + k):
                            curr.add(grid[ii][jj])

                    if len(curr) == 1:
                        res[i][j] = 0
                    else:
                        mn = float('inf')
                        s = sorted(curr)
                        for ii, v in enumerate(s):
                            if ii == 0:
                                continue
                            mn = min(mn, v - s[ii - 1])

                        res[i][j] = mn
        
        return res