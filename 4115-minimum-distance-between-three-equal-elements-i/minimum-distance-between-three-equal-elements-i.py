class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = inf

        for i in range(n):
            for j  in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] and nums[j] == nums[k]:
                        res = min(res, abs(i - j) + abs(j - k) + abs(i - k))

        return res if res != inf else -1  