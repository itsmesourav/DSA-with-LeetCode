class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        total = sum(grid[i][j] for j in range(m) for i in range(n))

        curr = 0
        for i in range(n):
            for j in range(m):
                curr += grid[i][j]
            if total - curr == curr:
                return True

        curr = 0
        for j in range(m):
            for i in range(n):
                curr += grid[i][j]
                if total - curr == curr:
                    return True
        return False