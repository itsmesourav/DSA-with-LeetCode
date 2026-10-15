
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        for start in range(n):
            seen = set()

            for end in range(start, n):
                seen.add(nums[end])
                distinct = len(seen)
                total += distinct * distinct

        return total
