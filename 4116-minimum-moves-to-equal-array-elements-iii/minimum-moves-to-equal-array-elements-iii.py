class Solution:
    def minMoves(self, nums: List[int]) -> int:
        res = 0
        mx = max(nums)
        for n in nums:
            res += mx - n
        return res