class Solution(object):
    def maxDepth(self, s):
        d = 0
        res = 0

        for c in s:
            if c == '(':
                d -= 1
            elif c ==')':
                d += 1
            res = max(res, abs(d))
            
        return res