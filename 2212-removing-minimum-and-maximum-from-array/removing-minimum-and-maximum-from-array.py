class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mn, mx = nums.index(min(nums)), nums.index(max(nums))
        l, r = min(mn, mx), max(mn, mx)
        return min(r + 1, n - l, l + 1 + n - r)