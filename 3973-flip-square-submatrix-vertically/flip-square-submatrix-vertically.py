class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        sub_row = 0
        for i in range(x, x + k):
            if sub_row == (x + k - x) // 2:
                break
            for j in range(y, y + k):
                grid[i][j], grid[x + k - 1 - sub_row][j] = grid[x + k - 1 - sub_row][j], grid[i][j]
            sub_row = sub_row + 1
        return grid