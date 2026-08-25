class Solution(object):
    def missingMultiple(self, nums, k):
        nums = set(nums)
        curr = k
        while curr in nums:
            curr += k
        return curr