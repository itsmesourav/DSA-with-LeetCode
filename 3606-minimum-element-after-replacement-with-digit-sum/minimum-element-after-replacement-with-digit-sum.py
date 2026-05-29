class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = inf

        for n in nums:
            sum =  0
            while n:
                sum += n % 10
                n //= 10
            res = min(res, sum)
        
        return res