from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[j][k] = max coins at current row, column j, with k neutralizations used
        dp = [[-float('inf')] * 3 for _ in range(n)]
        
        # Initialize (0,0)
        if coins[0][0] >= 0:
            dp[0][0] = coins[0][0]
        else:
            dp[0][0] = coins[0][0]  # no neutralization
            dp[0][1] = 0            # use 1 neutralization
        
        # First row
        for j in range(1, n):
            new = [-float('inf')] * 3
            for k in range(3):
                if dp[j-1][k] == -float('inf'):
                    continue
                
                if coins[0][j] >= 0:
                    new[k] = max(new[k], dp[j-1][k] + coins[0][j])
                else:
                    # take loss
                    new[k] = max(new[k], dp[j-1][k] + coins[0][j])
                    # neutralize
                    if k < 2:
                        new[k+1] = max(new[k+1], dp[j-1][k])
            dp[j] = new
        
        # باقي rows
        for i in range(1, m):
            new_dp = [[-float('inf')] * 3 for _ in range(n)]
            
            # first column
            for k in range(3):
                if dp[0][k] == -float('inf'):
                    continue
                
                if coins[i][0] >= 0:
                    new_dp[0][k] = max(new_dp[0][k], dp[0][k] + coins[i][0])
                else:
                    new_dp[0][k] = max(new_dp[0][k], dp[0][k] + coins[i][0])
                    if k < 2:
                        new_dp[0][k+1] = max(new_dp[0][k+1], dp[0][k])
            
            # rest columns
            for j in range(1, n):
                for k in range(3):
                    val = coins[i][j]
                    
                    # from top
                    if dp[j][k] != -float('inf'):
                        if val >= 0:
                            new_dp[j][k] = max(new_dp[j][k], dp[j][k] + val)
                        else:
                            new_dp[j][k] = max(new_dp[j][k], dp[j][k] + val)
                            if k < 2:
                                new_dp[j][k+1] = max(new_dp[j][k+1], dp[j][k])
                    
                    # from left
                    if new_dp[j-1][k] != -float('inf'):
                        if val >= 0:
                            new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k] + val)
                        else:
                            new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k] + val)
                            if k < 2:
                                new_dp[j][k+1] = max(new_dp[j][k+1], new_dp[j-1][k])
            
            dp = new_dp
        
        return max(dp[n-1])