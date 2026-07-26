class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()

        return max(
            nums[-1] * nums[-2] * nums[0-3],
            nums[0] * nums [1] * nums[0-1]
        )