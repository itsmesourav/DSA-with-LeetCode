from collections import defaultdict

class Solution(object):
    def findShortestSubArray(self, nums):
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