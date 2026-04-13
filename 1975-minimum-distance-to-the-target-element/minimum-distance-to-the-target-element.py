class Solution(object):
    def getMinDistance(self, nums, target, start):
        n = len(nums)
        res = float('inf')
        
        for i in range(n):
            if nums[i] == target:
                res = min(res, abs(i - start))
        
        return res
        