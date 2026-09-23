class Solution(object):
    def minOperations(self, nums, x):
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return len(nums)

        left = 0
        curr_sum = 0
        longest = -1

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                longest = max(longest, right - left + 1)

        if longest == -1:
            return -1

        return len(nums) - longest