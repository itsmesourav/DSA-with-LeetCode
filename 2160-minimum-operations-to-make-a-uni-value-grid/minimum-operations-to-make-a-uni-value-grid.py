class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n = len(grid)
        m = len(grid[0])
        arr = []
        rem = -1

        if n == 1 and m == 1:
            return 0
        
        for i in range(n):
            for j in range(m):
                if rem == -1:
                    rem = grid[i][j] % x
                elif grid[i][j] % x != rem:
                    return -1
                arr.append(grid[i][j])
        
        res = 0
        arr.sort()
        mid = arr[len(arr) // 2]
        for val in arr:
            res += abs(val -mid) // x
        
        return res