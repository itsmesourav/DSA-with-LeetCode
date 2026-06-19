class Solution(object):
    def largestAltitude(self, gain):
        res = 0
        acc = 0

        for g in gain:
            acc = acc + g
            res = max(res, acc)

        return res
        