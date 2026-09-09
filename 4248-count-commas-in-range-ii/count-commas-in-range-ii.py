class Solution(object):
    def countCommas(self, n):
        res = 0

        for c in range(1, 6):
           res += max(0, n - (1000**c - 1))

        return res