class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        ans = 0

        for x in nums:
            ans += abs(x - nums[mid])

        return ans