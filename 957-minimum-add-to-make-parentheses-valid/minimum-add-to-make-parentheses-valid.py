class Solution(object):
    def minAddToMakeValid(self, s):
        d = 0
        res = 0

        for c in s:
            if c == '(': d += 1
            else: d -= 1
            if d < 0:
                res += 1
                d = 0
        return res + abs(d)