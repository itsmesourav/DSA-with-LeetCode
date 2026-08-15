class Solution(object):
    def longestSubsequence(self, nums):
        n = len(nums)
        xor = 0
        z = 0

        for num in nums:
            xor ^= num
            if num == 0:
                z += 1
        
        if xor == 0:
            if z == n:
                return 0
            return n - 1
            
        return n