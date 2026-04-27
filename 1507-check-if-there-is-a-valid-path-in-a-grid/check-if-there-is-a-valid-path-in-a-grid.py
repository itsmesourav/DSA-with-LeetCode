class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dirs = {
            1: [(0, 1), (0, -1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)]
        }

        opposite = {
            (1, 0): (-1, 0),
            (-1, 0): (1, 0),
            (0, 1): (0, -1),
            (0, -1): (0, 1)
        }

        def dfs(i, j):
            if i == n - 1 and j == m - 1:
                return True

            for di, dj in dirs[grid[i][j]]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni == n or nj < 0 or nj == m or (ni, nj) in seen:
                    continue
                if opposite[(di, dj)] in dirs[grid[ni][nj]]:
                    seen.add((ni, nj))
                    if dfs(ni, nj):
                        return True
            
            return False

        n = len(grid)
        m = len(grid[0])
        seen = {(0, 0)}
        return dfs(0, 0)