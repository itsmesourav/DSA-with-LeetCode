class Solution(object):
    def maxProduct(self, n):
        d = []

        while n:
            d.append(n % 10)
            n //= 10
        
        d.sort()
        return d[-1] * d[-2]