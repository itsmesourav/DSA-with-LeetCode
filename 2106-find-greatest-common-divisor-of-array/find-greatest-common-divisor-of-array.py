from fractions import gcd
class Solution(object):
    def findGCD(self, nums):
        return gcd(min(nums), max(nums))