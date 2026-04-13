class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        res = inf

        for i in range(n):
            if nums[i] == target:
                res = min(res, abs(i - start))
        
        return res