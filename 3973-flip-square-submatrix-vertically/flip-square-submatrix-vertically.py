class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        sub_row = 0
        for i in range(x, x + k):
            if sub_row == (x + k - x) // 2:
                break
            for j in range(y, y + k):
                grid[i][j], grid[x + k - 1 - sub_row][j] = grid[x + k - 1 - sub_row][j], grid[i][j]
            sub_row = sub_row + 1
        return grid
        