class Solution(object):
    def smallestIndex(self, nums):
        for i, num in enumerate(nums):
            s = 0
            while num:
                s += num % 10
                num //= 10
            if s == i:
                return i
        return -1