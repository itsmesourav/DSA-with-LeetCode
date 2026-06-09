class Solution(object):
    def maxTotalValue(self, nums, k):
        mx, mn = float('-inf'), float('inf')

        for n in nums:
            mx = max(mx, n)
            mn = min(mn, n)
        
        return (mx - mn) * k