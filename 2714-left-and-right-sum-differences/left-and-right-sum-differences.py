class Solution(object):
    def leftRightDifference(self, nums):
        n =  len(nums)
        res = []
        left = 0
        right = sum(nums)

        for i in range(n):
            if i > 0:
                left += nums[i - 1]
            right -= nums[i]
            res.append(abs(left - right))

        return res
        