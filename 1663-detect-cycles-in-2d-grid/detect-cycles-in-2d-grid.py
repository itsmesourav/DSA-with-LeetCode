class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j, pi, pj,c):
            if grid[i][j] != c:
                return False
            if (i, j) in seen:
                return True
            seen.add((i, j))

            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if ni < 0 or ni == n or nj < 0 or nj == m or (ni, nj) == (pi, pj):
                    continue
                if dfs(ni, nj, i, j, c):
                    return True
            
            return False

        seen = set()
        for i in range(n):
            for j in range(m):
                if not (i, j) in seen:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        
        return False