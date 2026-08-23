from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            if start == nums[i]:
                ans.append(str(start))
            else:
                ans.append(f"{start}->{nums[i]}")

            i += 1

        return ans