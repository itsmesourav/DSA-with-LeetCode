class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        return gcd(mn, mx)