class Solution(object):
    def minMoves(self, nums):
        # m = minimun number:
        m = min(nums)
        ans = 0

        for x in nums:
            ans += x - m

        return ans