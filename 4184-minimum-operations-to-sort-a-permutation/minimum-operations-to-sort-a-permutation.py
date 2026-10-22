from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Check all left rotations without reversing
        for k in range(n):
            if all(nums[(i + k) % n] == i for i in range(n)):
                return min(k, n - k + 2) if k != 0 else 0

        # Check all left rotations after reversing
        rev = nums[::-1]
        for k in range(n):
            if all(rev[(i + k) % n] == i for i in range(n)):
                return min(k + 1, n - k + 1)

        return -1