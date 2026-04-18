class Solution:
    def mirrorDistance(self, n: int) -> int:
        r =str(n)[::-1]
        return abs(n - int(r))