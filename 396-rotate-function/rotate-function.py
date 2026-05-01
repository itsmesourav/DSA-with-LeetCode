class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        prev = 0
        total = sum(nums)

        for i in range(n):
            prev += nums[i] * i

        res = prev # f(0)
        for i in range(n - 1, 0, -1):
            prev = prev + (total - nums[i]) - (n - 1) * nums[i]
            res =  max(res, prev)
        
        return res
        