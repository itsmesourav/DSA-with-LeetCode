class Solution(object):
    def mirrorDistance(self, n):
        num = n
        r = 0
        while n:
            r = r * 10 + (n % 10)
            n //= 10
        return abs(num - r)