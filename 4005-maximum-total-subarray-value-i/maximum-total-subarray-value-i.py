class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mx, mn = -inf, inf

        for n in nums:
            mx = max(mx, n)
            mn = min(mn, n)
        
        return (mx - mn) * k