class Solution(object):
    def minSwaps(self, grid):
        n = len(grid)
        pos = [-1] * n
        
        # Find rightmost 1 in each row
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    pos[i] = j
                    break
        
        ans = 0
        
        for i in range(n):
            k = -1
            
            # Find a row we can bring up
            for j in range(i, n):
                if pos[j] <= i:
                    k = j
                    ans += j - i
                    break
            
            if k == -1:
                return -1
            
            # Bubble row k up to position i
            for j in range(k, i, -1):
                pos[j], pos[j - 1] = pos[j - 1], pos[j]
        
        return ans