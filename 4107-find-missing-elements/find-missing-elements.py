class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = set(nums)

        mn = min(nums)
        mx = max(nums)

        res = []
        for n in range(mn, mx + 1):
            if n not in nums:
                res.append(n)

        return res