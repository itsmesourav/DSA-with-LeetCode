class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        s = []

        for i in range(n):
            v = nums[i]
            l, r = i, i

            while s and s[-1][0] > nums[i]:
                lastv, lastl, lastr = s.pop()
                v = max(v, lastv)
                l = lastl
            s.append((v, l, r))
        
        for v, l, r in s:
            for i in range(l, r + 1):
                res[i] = v
        return res