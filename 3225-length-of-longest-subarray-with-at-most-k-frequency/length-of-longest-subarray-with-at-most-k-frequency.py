class Solution(object):
    def maxSubarrayLength(self, nums, k):
        n = len(nums)
        fm = defaultdict(int)

        res = 0
        l = 0
        for r in range(n):
            fm[nums[r]] += 1
            while l < r and fm[nums[r]] > k:
                fm[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
        