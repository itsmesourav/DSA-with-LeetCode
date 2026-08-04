class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = set(nums)

        mn, mx = float('inf'), float('-inf')
        for n in nums:
            mn = min(mn, n)
            mx = max(mx, n)

        res = []
        for n in range(mn, mx + 1):
            if not n in nums:
                res.append(n)

        return res