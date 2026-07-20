class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shift(grid):
            n = len(grid)
            m = len(grid[0])

            last = grid[-1][-1]

            for i in range(n):
                nlast = grid[i][-1]
                for j in range(m - 1, 0, -1):
                    grid[i][j] = grid[i][j - 1]
                grid[i][0] = last
                last = nlast
    
        for _ in range(k):
            shift(grid)
    
        return grid