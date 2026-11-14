class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        res = float('inf')

        for i in range(n):
            curr = 0

            for j in range(i, n):
                curr += nums[j]
                length = j - i + 1

                if length > r:
                    break

                if length >= l and curr > 0:
                    res = min(res, curr)

        return res if res != float('inf') else -1