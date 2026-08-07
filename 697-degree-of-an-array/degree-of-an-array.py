from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        first = {}
        last = {}

        for i, num in enumerate(nums):
            count[num] += 1
            if num not in first:
                first[num] = i
            last[num] = i

        degree = max(count.values())
        ans = len(nums)

        for num in count:
            if count[num] == degree:
                ans = min(ans, last[num] - first[num] + 1)

        return ans