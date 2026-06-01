class Solution(object):
    def minimumCost(self, cost):
        n = len(cost)
        cost.sort()
        res = 0

        count = 1
        for i in range(n - 1, -1, -1):
            if count != 3:
                res += cost[i]
                count += 1
            else:
                count = 1
        
        return res