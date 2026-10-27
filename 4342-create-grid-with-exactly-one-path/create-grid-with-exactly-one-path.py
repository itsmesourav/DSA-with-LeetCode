class Solution(object):
    def createGrid(self, m, n):
        grid = [['#'] * n for _ in range(m)]

        for i in range(m):
            grid[i][0] = '.'
        for j in range(n):
            grid[-1][j] = '.'

        return ["".join(row) for row in grid]