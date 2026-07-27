class Solution(object):
    def maxProduct(self, nums):
        mx = 0
        secondmx = 0

        for n in nums:
            if n > mx:
                secondmx = mx
                mx = n
            else:
                secondmx = max(secondmx, n)
            
        return (mx - 1) * (secondmx - 1)