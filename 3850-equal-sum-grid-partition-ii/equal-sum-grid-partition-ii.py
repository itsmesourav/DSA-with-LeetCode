class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(g):
            nn = len(g)
            mm = len(g[0])

            curr = 0
            seen = {}
            for i in range(nn - 1):
                for j in range(mm):
                    v = g[i][j]
                    curr += v
                    if v in seen:
                        seen[v][1] = (i, j)
                    else:
                        seen[v] = [(i, j), (i, j)]
            
                diff = total - curr - curr
                if diff == 0:
                    return True
                if -diff in seen:
                    fr, fc = seen[-diff][0]
                    lr, lc = seen[-diff][1]
                    if mm > 1 and i + 1 > 1:
                        return True
                    if mm > 1 and i + 1 == 1 and (fc == 0 or lc == mm - 1):
                        return True
                    if mm == 1 and (fr == 0 or lr == i):
                        return True
    
        n = len(grid)
        m = len(grid[0])

        total = sum(grid[i][j] for j in range(m) for i in range(n))
        if check(grid) or check(grid[::-1]): 
            return True
    
        # trnaspose grid
        # ng = []
        # for j in range(m):
        #     nr = []
        #     for i in range(n):
        #          nr.append(grid[i][j])
        #     ng.append(nr)

        grid = list(zip(*grid))

        if check(grid) or check(grid[::-1]):
            return True
        return False