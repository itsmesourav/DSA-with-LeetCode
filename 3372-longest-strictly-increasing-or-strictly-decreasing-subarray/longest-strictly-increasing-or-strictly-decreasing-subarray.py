class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            curr = []
            for j in range(i, n):
                curr.append(nums[j])
                if (
                    all(curr[idx] > curr[idx - 1] for idx in range(1, len(curr))) or
                    all(curr[idx] < curr[idx - 1] for idx in range(1, len(curr)))
                ):
                    res = max(res, j - i + 1)
        
        return res